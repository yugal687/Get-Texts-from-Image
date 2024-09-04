

# Extract texts from image
from pytesseract import pytesseract
from PIL import Image

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"./text.png"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img) 

print(text[:-1])

