import cv2
import pytesseract
from PIL import Image

# ONLY for Windows: set Tesseract path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 1: Load image
img = cv2.imread("document.jpg")

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Apply threshold to improve OCR
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# Step 4: Extract text
text = pytesseract.image_to_string(gray)

# Step 5: Print text
print("Extracted Text:\n", text)

# Step 6: Save text to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Optional: Show processed image
cv2.imshow("Processed Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
