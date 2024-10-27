Here’s the updated project setup and usage guide for **AruVision**, including the note about ongoing development:

---

# AruVision (Augmented Reality Using OpenCV and Python)

## Configuration
- **Python Version**: 3.11.7
- **Operating System**: Windows 10
- **Install External Libraries**:
   - Install all required libraries in the current directory by running:
   ```bash
   pip install -r requirements.txt
   ```
   - For OpenGL and Pygame (used to load textures), install them in your Python environment. You can find the corresponding libraries in the `ExternalConfig` folder. Copy them to your Python environment and install directly, for example:
   ```bash
   python -m pip --user pygame-1.9.6-cp37-cp37m-win_amd64.whl
   ```

## Getting Camera Information
### Calibration
In the program, we need your camera's intrinsic matrix and distortion coefficients. We will use chessboard calibration to obtain these:
1. Download a chessboard image. A sample image is provided [here](chessboard.png). Capture at least 20 photos using your camera and save them to the `ChessBoardSet` directory.
2. Execute `CameraCalibration.py` to find your camera information, which will be saved in `CameraParameter/data1.txt`.

## Running the Program
1. Copy the camera intrinsic matrix and distortion coefficients into the corresponding parameters in `AR_entrance.py`.
2. Run `AR_entrance.py` and choose models saved in the `Models` directory.
3. Use the **'+'** or **'-'** keys to scale the model size during execution.

**Note**: You can generate the ArUco markers yourself using an [aruco generator](http://chev.me/arucogen/).

## Current Development Status
**AruVision is still under development and not fully ready**, as there are a few compatibility issues that need to be resolved. Your feedback and contributions are welcome!

## Contribute
If you're interested in OpenCV, OpenGL, and AR, feel free to become a contributor. I will respond as soon as possible.

## Contact
- **If you like this project, please give it a star and fork it! 😊**
