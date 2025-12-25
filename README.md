# Next-Gen-Human-Computer-Interaction-Air-Drawing


## Project Overview
The Hand Controlled Air Drawing System is a computer vision–based application that allows users to draw on a virtual canvas using hand gestures without touching the screen. A webcam captures live hand movements, and the system converts these gestures into drawing actions in real time. This project demonstrates an intuitive approach to human–computer interaction using hand landmark detection.

---

## Objectives
- Enable touch-free drawing using hand gestures  
- Detect and track hand movements in real time  
- Provide gesture-based color selection and erasing  
- Build a simple, interactive, and user-friendly drawing interface  

---

## Technologies Used
- Python 3.12  
- OpenCV  
- MediaPipe Tasks API  
- NumPy  

---

## Working Principle
1. The webcam captures live video frames.
2. MediaPipe detects 21 hand landmarks in each frame.
3. Finger states (up or down) are determined by comparing fingertip and joint positions.
4. Gestures are interpreted to control drawing, color selection, or erasing.
5. The drawing is rendered on a virtual canvas in real time.

---

## Gesture Controls

| Gesture | Action |
|--------|--------|
| Index finger up | Draw |
| Index + Middle fingers up | Green color |
| Index + Ring fingers up | Blue color |
| Index + Pinky fingers up | Red color |
| All fingers up | Eraser (thick) |
| Press **C** | Clear canvas |
| Press **ESC** | Exit application |

---

## Eraser Feature
The eraser uses a larger stroke thickness compared to the drawing brush. This allows faster and more effective clearing of the canvas, improving usability and reducing effort during corrections.

---

## Project Structure

hand gesture/
│
├── air_drawing.py
├── hand_landmarker.task
└── README.md


---

## Installation

Install the required Python libraries:

Download the MediaPipe hand landmark model from:

Place the downloaded `hand_landmarker.task` file in the same directory as `air_drawing.py`.

---

## How to Run
1. Open PowerShell or Command Prompt in the project directory.
2. Run the following command:
3. Ensure your webcam is enabled and accessible.

---

## Features
- Real-time hand tracking  
- Touch-free drawing interface  
- Gesture-based color selection  
- Thick eraser for efficient clearing  
- Smooth performance with low latency  
- No external hardware required  

---

## Applications
- Digital sketching and creative drawing  
- Virtual whiteboards  
- Interactive teaching and learning tools  
- Gesture-based user interfaces  

---

## Future Enhancements
- Dynamic brush and eraser size control  
- On-screen color palette display  
- Saving drawings as image files  
- Multi-hand support  
- Gesture lock to reduce accidental changes  

---

## Conclusion
The Hand Controlled Air Drawing System showcases the effective use of computer vision for natural and intuitive human–computer interaction. By combining MediaPipe’s accurate hand landmark detection with OpenCV’s drawing capabilities, the system provides a responsive and engaging air-drawing experience suitable for educational, creative, and interactive applications.



## Team Members
- Narendran B
- Kamalesh S V
- Alagu Nachiyar K
