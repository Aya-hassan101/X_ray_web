#  BoneFracture AI - Advanced Diagnostic Suite

An AI-powered desktop application for detecting bone fractures from X-ray images using Deep Learning and a modern GUI built with CustomTkinter.

---

##  Project Overview

This project is a **medical imaging assistant** that uses a trained deep learning model to analyze X-ray images and classify whether a bone fracture is present or not.

The system provides a simple and user-friendly interface that allows users to upload images and instantly receive AI-based predictions with confidence scores.

---

## Features

- 🖥️ Modern GUI using `CustomTkinter`
- 📷 Upload and preview X-ray images
- 🤖 Deep Learning model for fracture detection
- 📊 Confidence score for predictions
- 🌙 Dark / Light / System theme support
- ⚡ Fast real-time inference

---

##  Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- PIL (Pillow)
- CustomTkinter
- Tkinter (file dialog)

---

## How It Works

1. User uploads an X-ray image  
2. Image is preprocessed (resize + normalization)  
3. CNN model (`Bone_model.h5`) predicts result  
4. System displays:
   - Fracture detected / Not detected  
   - Confidence level  
   - Image preview in GUI  

---

## Model Input Processing

- Resize image → `150 x 150`
- Normalize pixel values (0–1)
- Expand dimensions for model input
- Binary classification output

---


pip install tensorflow opencv-python pillow customtkinter numpy
