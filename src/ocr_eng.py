import os
import pytessrcat # This library is used for OCR to extract text from images.
from PIL import Image # This library is used to open and manipulate images

class OCREngine:
    @staticmethod
    def extract_text(file_path):
        try:
            image = Image.open(file_path) # open Images
            text = pytessrcat.image_to_string(image) # extract text from the image.
            return text # The extracted text is returned as the result
        except Exception as e:
            return str(e)