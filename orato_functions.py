from PIL import Image

import os
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/tessdata/'

import pytesseract
from gtts import gTTS

import cv2
from pydub import AudioSegment
from deep_translator import GoogleTranslator
from playsound import playsound

import uuid



def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_path = f'processed_{uuid.uuid4().hex}.png'
    cv2.imwrite(processed_path, gray)
    return processed_path

def text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"[OCR Error: {str(e)}]"

def speak_text(text, output_path="output.mp3", language="en"):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save(output_path)
        playsound(output_path)
    except Exception as e:
        print(f"[TTS Error: {e}]")


'''  if speed != 1.0:
        sound = AudioSegment.from_file(filename)
        new_frame_rate = int(sound.frame_rate * speed)
        altered_sound = sound._spawn(sound.raw_data, overrides={
            "frame_rate": new_frame_rate
        }).set_frame_rate(sound.frame_rate)
        altered_sound.export(filename, format="mp3")

def translate_text(text, target_lang='en'):
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        return f"[Translation Error: {str(e)}]" '''
