import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('download.png',-1)
cv2.imshow('image',img)
text=pytesseract.image_to_string(img)
print(text)
cv2.waitKey(0) 
cv2.destroyAllWindows()
