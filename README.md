# 🎨 Real-Time Color Recognition

A real-time computer vision project built with **Python**, **OpenCV**, and **NumPy**. This application detects **Red**, **Green**, and **Blue** objects through a webcam, draws bounding boxes around them, and displays the detected color name in real time.

---

## 🚀 Features

- 🎥 Real-time webcam processing
- 🔴 Detect Red objects
- 🟢 Detect Green objects
- 🔵 Detect Blue objects
- 📦 Draw bounding boxes around detected objects
- 🏷 Display detected color names
- 🧹 Noise reduction using morphological operations
- ⚡ Fast real-time performance
- ❌ Exit using **Q** or **ESC**

---

## 🛠 Technologies Used

- Python 3.11
- OpenCV
- NumPy
- Visual Studio Code
- Anaconda

---

## 📂 Project Structure

```text
opencv-color-recognition/
│
├── color_recognition.py
├── README.md
└── requirements.txt
```

---

## ⚙ Installation

Create a virtual environment:

```bash
conda create -n opencv-env python=3.11
conda activate opencv-env
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

```bash
python color_recognition.py
```

---

## 🧠 How It Works

1. Opens the webcam.
2. Converts each frame from **BGR** to **HSV**.
3. Creates color masks for Red, Green, and Blue.
4. Removes small image noise.
5. Detects object contours.
6. Draws bounding boxes around detected objects.
7. Displays the detected color name.
8. Shows the processed video in real time.

---

## 🎯 Supported Colors

| Color | Status |
|-------|--------|
| 🔴 Red | ✅ |
| 🟢 Green | ✅ |
| 🔵 Blue | ✅ |

---

## 📸 Screenshots

_Add screenshots here after uploading them to the `images` folder._

Example:

```markdown
![Blue Detection](images/demo1.png)
```

---

## 📦 Requirements

```
opencv-python
numpy
```

Or install them manually:

```bash
pip install opencv-python numpy
```

---

## 👨‍💻 Author

**Adel Bin Ateeq**

Computer Engineering Student

Interested in:
- Artificial Intelligence
- Cybersecurity
- Cloud Computing

GitHub:
https://github.com/AdelAteeq

---

## ⭐ Future Improvements

- Detect additional colors.
- Improve detection under different lighting conditions.
- Add object tracking.
- Support more advanced computer vision techniques.

---

## 📄 License

This project is created for educational purposes.
