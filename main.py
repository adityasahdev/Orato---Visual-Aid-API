from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
import uuid
import os

from orato_functions import text_from_image, preprocess_image, speak_text

app = FastAPI()


@app.post("/orato/")
async def orato(
                image: UploadFile = File(...),
                ):
       # Create a temporary file path
    temp_filename = f"temp_{uuid.uuid4().hex}.jpg"
    temp_filepath = os.path.join("temp_uploads", temp_filename)

    # Ensure the temp_uploads directory exists
    os.makedirs("temp_uploads", exist_ok=True)

    # Save the file to disk
    with open(temp_filepath, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
 
    preprocessed_image = preprocess_image(temp_filepath)
    text = text_from_image(preprocessed_image)
    print(text)


    if not text.strip():
        return {"error": "No text found in the image."}

    speak_text(text,'/Users/adityaahdev/Desktop/Orato/output.mp3')

    return FileResponse(path='/Users/adityaahdev/Desktop/Orato/output.mp3', media_type="image/jpeg", filename="output.jpg")

