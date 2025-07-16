# Orato 🗣️📸

**Orato** is a computer vision-based speech generation project that allows users to upload an image, extract the text from it using Optical Character Recognition (OCR), and then convert the extracted text into speech using Text-to-Speech (TTS) technology. Built using Python and FastAPI, Orato is a lightweight REST API application designed for accessibility, learning, and real-world prototyping.

---

## 🚀 Features

- ✅ Upload an image and extract text using Tesseract OCR
- ✅ Preprocess the image with OpenCV to improve text detection
- ✅ Convert extracted text into speech with gTTS
- ✅ Returns an `.mp3` audio file for playback
- ✅ Simple and modular backend architecture

---

## 🧠 Tech Stack

- **FastAPI** – Backend API framework
- **Tesseract OCR** – Text extraction engine
- **gTTS** – Google Text-to-Speech for audio synthesis
- **OpenCV** – Image preprocessing
- **Pillow (PIL)** – Image handling
- **Pydub** – Audio file manipulation
- **Playsound** – Audio playback

---

## 📁 Project Structure

Orato/
├── main.py # FastAPI application
├── orato_functions.py # Core logic for OCR and TTS
├── temp_uploads/ # Temporary image storage
├── output.mp3 # Final audio output
└── README.md # Project documentation

## 💡 Motivation

I created Orato as a side project to explore the integration of OCR and speech synthesis using Python APIs.
The goal was to build a minimal, functioning prototype for accessibility technology that bridges vision and audio. 
It also helped me improve my understanding of REST API development, computer vision, and working with media files in Python.


## 🔮 Future Improvements

Add language translation and multilingual support
Add speech speed and pitch control
Build a web UI for drag-and-drop uploads
Add camera input and support for real-time processing
Integrate Whisper or other advanced OCR models

