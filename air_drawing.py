import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks import python

# ----------------------------------
# Load MediaPipe Hand Landmarker
# ----------------------------------
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

# ----------------------------------
# Webcam and Canvas
# ----------------------------------
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

prev_x, prev_y = 0, 0
draw_color = (255, 0, 0)  # Default: Blue

# Thickness settings
brush_thickness = 5
eraser_thickness = 30   # 👈 thicker eraser

# ----------------------------------
# Main Loop
# ----------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        landmarks = result.hand_landmarks[0]
        h, w, _ = frame.shape

        # Convert landmarks to pixel coordinates
        points = [(int(l.x * w), int(l.y * h)) for l in landmarks]

        # Fingertips
        index = points[8]
        middle = points[12]
        ring = points[16]
        pinky = points[20]

        # ----------------------------------
        # Finger UP / DOWN detection
        # ----------------------------------
        index_up = index[1] < points[6][1]
        middle_up = middle[1] < points[10][1]
        ring_up = ring[1] < points[14][1]
        pinky_up = pinky[1] < points[18][1]

        # ----------------------------------
        # Color Selection (Stable Gestures)
        # ----------------------------------
        if index_up and middle_up and ring_up and pinky_up:
            draw_color = (0, 0, 0)        # Eraser
        elif index_up and pinky_up:
            draw_color = (0, 0, 255)      # Red
        elif index_up and ring_up:
            draw_color = (255, 0, 0)      # Blue
        elif index_up and middle_up:
            draw_color = (0, 255, 0)      # Green

        # ----------------------------------
        # Drawing Logic
        # ----------------------------------
        if index_up and not middle_up:
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = index

            # Choose thickness
            if draw_color == (0, 0, 0):      # Eraser
                thickness = eraser_thickness
            else:
                thickness = brush_thickness

            cv2.line(canvas, (prev_x, prev_y), index, draw_color, thickness)
            prev_x, prev_y = index
        else:
            prev_x, prev_y = 0, 0

    # ----------------------------------
    # Merge Canvas with Frame
    # ----------------------------------
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_BGR2RGB)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("Hand Controlled Air Drawing", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
