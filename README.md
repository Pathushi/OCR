This project is a small Python-based OCR (Optical Character Recognition) tool. 
It reads text from images and saves the extracted text to a file.

Features
- Reads text from an image file.
- Converts image to grayscale and applies thresholding for better OCR accuracy.
- Prints extracted text to the terminal.
- Saves extracted text to output.txt.
- Displays processed image.

## Requirements
- Python 3.x
- Libraries:
  - OpenCV (`pip install opencv-python`)
  - Pillow (`pip install pillow`)
  - pytesseract (`pip install pytesseract`)
- Tesseract OCR Engine installed:
  - Windows: https://github.com/tesseract-ocr/tesseract
  - Mac: `brew install tesseract`
  - Linux: `sudo apt install tesseract-ocr`

## Setup Instructions
1. Clone or download this repository.
2. Place the image you want to extract text from in the project folder (e.g., document.jpg).
3. Open the terminal in the project folder.

4. Install required Python packages:
   `pip install opencv-python pillow pytesseract`
5. Set the correct path to Tesseract in the code (Windows only):
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

