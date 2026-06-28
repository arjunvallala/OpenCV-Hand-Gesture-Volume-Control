# Hand Gesture Volume Control using OpenCV & MediaPipe

Control your computer's system volume using hand gestures captured through a webcam. This project uses **MediaPipe Hands** for real-time hand landmark detection, **OpenCV** for computer vision, and **Pycaw** to control the Windows system volume.

---

## Features

* 🎥 Real-time webcam hand tracking
* ✋ Detects thumb and index finger fingertips
* 📏 Measures the distance between fingertips
* 🔊 Controls Windows system volume based on finger distance
* 📊 Displays a real-time volume bar and percentage
* ⚡ Shows FPS (Frames Per Second)

---

## Technologies Used

* Python 3.x
* OpenCV
* MediaPipe
* NumPy
* Pycaw
* Math
* Windows Core Audio API

---

## Project Structure

```
Hand-Gesture-Volume-Control/
│
├── HandTrackingModule.py
├── VolumeControl.py
├── requirements.txt
├── README.md
├── assets/
│   ├── demo.gif
│   └── screenshot.png
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Hand-Gesture-Volume-Control.git
```

### 2. Navigate into the project

```bash
cd Hand-Gesture-Volume-Control
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python VolumeControl.py
```

---

## How It Works

1. Webcam captures video frames.
2. MediaPipe detects the hand and returns 21 landmarks.
3. The positions of the thumb tip (Landmark 4) and index finger tip (Landmark 8) are extracted.
4. The Euclidean distance between these landmarks is calculated.
5. The distance is mapped to the system volume range using NumPy interpolation.
6. Pycaw updates the Windows master volume in real time.
7. OpenCV displays the live video along with the volume bar and FPS.

---

## Demo

### GIF

Place your demo GIF here.

```
assets/demo.gif
```

---

### Screenshot

Place a screenshot here.

```
assets/screenshot.png
```

---

## Future Improvements

* Gesture smoothing to reduce jitter
* Multi-hand gesture support
* Cross-platform audio control
* Gesture recognition using machine learning
* GUI for sensitivity adjustment

---

## License

This project is licensed under the MIT License.
