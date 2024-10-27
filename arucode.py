

import cv2
import numpy as np

# Define the dictionary and parameters
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the markers
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # Draw detected markers
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        print("Detected markers: ", ids)
    else:
        print("No markers detected")

    # Display the resulting frame
    cv2.imshow('Real-Time ArUco Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
