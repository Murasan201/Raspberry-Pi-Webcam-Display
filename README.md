
# Webcam Display on Raspberry Pi 5

A simple Python program to capture and display video from a webcam connected to a Raspberry Pi 5 in real-time using OpenCV. The program supports general USB webcams, including but not limited to the Logitech C270.

## Project Details

- **File Name**: `camera_display.py`
- **Description**: Displays video feed from an attached USB webcam in real-time. The display can be closed by pressing the "q" key.

## Requirements

- **Hardware**: Raspberry Pi 5 with a compatible USB webcam
- **Software**: Python 3, OpenCV library (`cv2`)

## Installation

1. Install OpenCV if it's not already installed:
   ```bash
   pip install opencv-python
   ```
2. Clone this repository and navigate to the directory.

3. Run the program:
   ```bash
   python camera_display.py
   ```

## Usage

- Connect a USB webcam to the Raspberry Pi 5.
- Run the program as instructed above.
- The video feed should appear in a window labeled "Webcam Display."
- Press "q" to quit the program.

## Notes

This program is designed for use with the Logitech C270 webcam but also supports other general USB webcams. Compatibility may vary based on the specific model and its driver support on Raspberry Pi.

## Author

Created by **Murasan Lab**  
For more projects and information, visit [Murasan Lab's official website](https://murasan-net.com/).
