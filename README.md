#   Phalanx-Vectorized Bio-Kinetic Optoelectronic Modulation System (PV-BOMS) 
---
### *Codename: The "Aggressive" LED Controller*

### *Because sometimes, a normal light switch is just too polite.*

Ever wanted to tell your room to "shut up" or "lighten up" without saying a word? This project combines high-tech computer vision with low-brow social gestures to give you the ultimate power over a single LED.

---

## 📸 Proof of Concept

<div align="center">
  <img src="Output/Screenshot 2026-04-22 120332.png" width="400" alt="Gesture Detection Dashboard">
  <p><i>The "Advanced" Dashboard</i></p>
  
  <br>

  <video width="400" controls muted loop>
    <source src="Output/bandicam%202026-04-08%2011-08-52-727.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p><i>C-TRACKER</i></p>
</div>

---

## 🤔 What is this?

The **APV-BOMS** is a state-of-the-art **Spite-Based Automation System**. Utilizing **Heuristic Phalangeal Landmark Vectorization** via **MediaPipe** and **OpenCV**, we perform real-time spatial analysis of hand geometry. When the system identifies a specific vertical phalanx-vector orientation (informally known as "The Bird"), it triggers an asynchronous serial signal to an **Arduino** to modulate the photonic output of a semiconductor diode (the LED).

### Why?
- **Efficiency**: Why walk 3 steps to a switch when you can flip it off from your desk?
- **Catharsis**: Release your daily frustration while staying productive.
- **Science**: We are quantitatively analyzing the Euclidean ratio of the middle phalangeal tip relative to the metacarpophalangeal base. It's essentially a PhD thesis in kinetic social commentary.

---

## 🛠️ The Tech Stack

- **Python 3.x**: The brains.
- **OpenCV**: To see your frustration.
- **MediaPipe**: To calculate exactly how much you mean it.
- **Arduino**: The muscle (toggling pin 11).

---

## 🚀 How to Launch the Spite-Box

1.  **Hardware**: Plug your Arduino into `COM7` (or change it in `capture.py`). Make sure an LED is on Pin 11.
2.  **Dependencies**:
    ```bash
    pip install opencv-python mediapipe pyserial numpy
    ```
3.  **Flash the Arduino**: Upload `hardware_Sketch/ard.ino` to your board.
4.  **Engage**:
    ```bash
    python capture.py
    ```
5.  **Gesture**: You know what to do. 🖕

---

## ⚠️ Safety Warning

- **Do not** use this during Zoom calls with your boss.
- **Do not** point it at your mother.
- The system has a **1-second cooldown** to prevent accidental "strobe-light-of-rage" effects.

---

*Created with ❤️ by jimbru.*
