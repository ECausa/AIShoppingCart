# IT254-Arduino-Project  
## AI Shopping Cart – YOLO Price Detection & Arduino Alert System

---

## Overview

The AI Shopping Cart is a prototype that allows customers to add items to their basket as long as the total remains under a fixed spending limit. A camera combined with AI-based object detection identifies items such as fruits, vegetables, and prepared foods as they appear in the cart. The system calculates a running total based on predefined prices and provides an audible alert when the limit is exceeded.

This project demonstrates the practical integration of computer vision, real-time data processing, and physical hardware feedback in a retail environment.

---

## Project Description

The system monitors a live camera feed and detects grocery items using a YOLOv8 model. As products enter or leave the frame, their associated prices are added or removed from the total. When the total passes the defined limit, an Arduino triggers a buzzer to notify the customer that the promotional threshold has been exceeded.

The goal is not perfect accuracy, but a responsive and interactive proof-of-concept for smart retail experiences.

---

## Core Features

- Real-time item recognition using AI and live video feed  
  - Detects items such as fruits, vegetables, and common grocery products  
- Dynamic price calculation based on detected objects  
- Live total displayed on the video stream  
- Enforced spending limit for promotional scenarios  
- Hardware alert system using Arduino and buzzer  
- Threshold-based warning to prevent overspending  

---

## System Requirements

### Hardware
- USB webcam (or compatible camera module)
- Arduino board (Uno, Nano, or similar)
- 1 Passive Buzzer
- 2-3 Male to male jumper wires
- USB cable connection between Arduino and computer

### Software & Libraries
Installed manually (no requirements file included):
- Python 3.11
- ultralytics  
- opencv-python  
- pyserial  

Install with:
```bash
pip install ultralytics opencv-python pyserial
````
* See Board_example.mp4 for an example setup of the Arduino board
---

## How It Works

1. The camera captures a continuous video feed.
2. YOLOv8 detects objects in each frame.
3. Only objects listed in `labels.txt` are processed.
4. Each detected item is matched to a price in the price map.
5. The combined total is calculated in real time.
6. If the total exceeds the defined threshold:
   * A signal is sent to the Arduino.
   * The buzzer plays an alert tone.

---

## Configuration

### Spending Threshold

Set inside the Python script:

```python
THRESHOLD = 5.00
```

### Pricing Data

Prices are defined directly in the `price_map` dictionary and represent estimated averages for demonstration purposes.

### Label Filtering

The `labels.txt` file determines which detected objects are eligible for pricing and tracking.

---

## File Structure

* yolo.py
  Core Python script handling detection, pricing, and Arduino communication
* labels.txt
  List of object labels that should be recognized and priced
* yolov8n.pt
  Pre-trained YOLO model weights
* Arduino Sketch
  Controls buzzer activation in response to serial commands

---

## Instructions
1. Download zip from Github and extract it then extract the arduino_code zip in it
2. Set up arduino 
   - Put passive buzzer on breadboard, both pins should be in row E
   - Put jumper wires on either sides aligned with the columns that the buzzer pins are in
   - Plug one wire into ground and the other wire into digital pin 8 (it doesnt matter which sides of the buzzer pins you plug it into) 
3. Plug arduino into computer's USB and upload the provided arduino code on to the device using arduinos IDE make sure to close it after upload
4. Open folder in a Python IDE and select yolo.py
5. Install packages in terminal (pip install ultralytics opencv-python pyserial)
6. Change port to needed port and run yolo.py
7. Place items in the camera's field of view.
8. The system identifies items and updates the total.
9. When the price limit is exceeded, the buzzer activates.
10. Removing items lowers the total and resets the alert trigger.

---

## Notes

* Total price is recalculated each frame based on current detections.
* Items are counted only while visible in the frame.
* Persistent object tracking is not implemented.
* Designed as a demonstration system, not for commercial accuracy.

---

## Potential Enhancements

* Persistent object tracking to prevent duplicate counting
* Barcode or RFID integration for higher accuracy
* Dynamic pricing via database or API
* Multi-tier alerts for different price levels
* GUI control panel for threshold and pricing management
* Cloud-based analytics for user behavior tracking

---

## Use Case

This system simulates a promotional shopping environment where customers are encouraged to stay within a budget. It provides immediate feedback, creating an engaging and interactive retail experience while demonstrating how AI can support real-world automation scenarios.
