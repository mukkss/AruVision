import numpy as np
import cv2
import glob
import os

# Termination criteria for the iterative algorithm to find the corner sub-pixel accuracy.
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Define the dictionary of ArUco markers to be detected.
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

# Arrays to store object points (3D points in real world) and image points (2D points in image plane) from all the images.
objpoints = []
imgpoints = []

# Load all images in the specified directory.
images = glob.glob('./ArUcoSet/*.jpg')

# Create output directories if they do not exist.
os.makedirs('./ArUcoMarkedSet', exist_ok=True)
os.makedirs('./CameraParameter', exist_ok=True)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect ArUco markers in the image.
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # If markers are detected, store the object points and image points.
    if ids is not None:
        # Define the object points for each detected marker.
        objpoints.extend([np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]], dtype=np.float32)] * len(ids))
        imgpoints.extend(corners)

        img_name = os.path.basename(fname)
        
        # Draw the detected markers on the image.
        img = cv2.aruco.drawDetectedMarkers(img, corners, ids)
        # Save the marked image to the output directory.
        cv2.imwrite(os.path.join('./ArUcoMarkedSet', img_name), img)

# Ensure that at least one image was successfully processed before attempting calibration.
if objpoints:
    # Use the first image to get the shape for the gray image.
    gray_shape = cv2.cvtColor(cv2.imread(images[0]), cv2.COLOR_BGR2GRAY).shape[::-1]
    # Perform camera calibration.
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_shape, None, None)

    # Get the optimal new camera matrix.
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, gray_shape, 1, gray_shape)

    # Write the camera parameters to a file.
    with open('./CameraParameter/data1.txt', 'w') as f:
        f.write('Mtx:\n')
        np.savetxt(f, newcameramtx, fmt='%.2f')
        
        f.write('\nRvecs:\n')
        f.write(str(rvecs))
        
        f.write('\nTvecs:\n')
        f.write(str(tvecs))
        
        f.write('\nDist:\n')
        np.savetxt(f, dist, fmt='%.2f')

# Clean up and close any OpenCV windows.
cv2.destroyAllWindows()
