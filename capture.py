import cv2
import mediapipe as mp
import serial
import time


import math

import numpy as np


try:
    arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
    time.sleep(2) 
    status_msg = "SERIAL: CONNECTED"
except:
    status_msg = "SERIAL: DISCONNECTED"


mp_hands = mp.solutions.hands

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def get_dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

camera = cv2.VideoCapture(1)
last_state = False
prev_time = 0

while camera.isOpened():
    ret, frame = camera.read()
    if not ret: break

    # FPS Calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    h, w, c = frame.shape
    black_panel = np.zeros((h, w, 3), dtype=np.uint8)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture_text = "SYSTEM IDLE"
    color = (0, 255, 0)
    ratio = 0.0
    conf = 0.0

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
           
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
            mp_draw.draw_landmarks(black_panel, hand_lms, mp_hands.HAND_CONNECTIONS)

           
            p9, p10, p11, p12 = hand_lms.landmark[9], hand_lms.landmark[10], hand_lms.landmark[11], hand_lms.landmark[12]
            
            base_to_tip = get_dist(p9, p12)
            actual_len = get_dist(p9, p10) + get_dist(p10, p11) + get_dist(p11, p12)
            ratio = base_to_tip / actual_len if actual_len > 0 else 0
            
            
            is_up = ratio > 0.95 and p12.y < p9.y
            if is_up:
                gesture_text = "TRIGGER ACTIVE"
                color = (0, 0, 255)

            
            if is_up != last_state:
                if is_up and 'arduino' in locals():
                    arduino.write(b'1')
                last_state = is_up

           
            for i, lm in enumerate(hand_lms.landmark):
               
               #metric
               #
                x_pos = 20 if i < 11 else 220
                y_pos = 180 + ((i % 11) * 25)
                cv2.putText(black_panel, f"L{i}: {lm.x:.2f},{lm.y:.2f},{lm.z:.2f}", 
                            (x_pos, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (150, 150, 150), 1)

    
    cv2.putText(black_panel, "--- C TRACKER ---", (20, 40), 1, 1.5, (255, 255, 255), 2)
    
    cv2.putText(black_panel, f"STATUS: {status_msg}", (20, 105), 1, 1.2, (200, 200, 200), 1)
    cv2.putText(black_panel, f"RATIO: {ratio:.4f}", (20, 135), 1, 1.2, color, 1)
    
    
    cv2.rectangle(black_panel, (200, 120), (w-20, 140), (40, 40, 40), -1)
    cv2.rectangle(black_panel, (200, 120), (200 + int(ratio * (w-220)), 140), color, -1)

    
    cv2.putText(black_panel, "RAW LANDMARK LOG (X, Y, Z):", (20, 170), 1, 1, (255, 255, 255), 1)

    
    combined = np.hstack((frame, black_panel))
    cv2.imshow('Advanced Gesture Dashboard', combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()