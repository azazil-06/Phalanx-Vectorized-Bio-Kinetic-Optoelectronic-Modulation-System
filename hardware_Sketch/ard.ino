const int ledPin = 11;
bool ledState = true;

// --- Timing Variables ---
unsigned long lastTriggerTime = 0;   // Stores the last time the LED was toggled
const unsigned long cooldown = 1000; // Minimum time between toggles (1 second)

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState ? HIGH : LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    
    if (cmd == '1') {
      unsigned long currentTime = millis();
      
      // Only toggle if 1 second has passed since the last toggle
      if (currentTime - lastTriggerTime >= cooldown) {
        ledState = !ledState;
        digitalWrite(ledPin, ledState ? HIGH : LOW);
        
        // Update the timestamp to current time
        lastTriggerTime = currentTime;
        
        Serial.println("Toggle Successful");
      } else {
        // Optional: Feedback that the command was ignored
        Serial.println("Ignored: Cooldown active");
      }
    }
  }
}