#Extraction notes 3 scannedpdf
#Same procedure as the first one. Only difference is importing OCR library to extract text from scanned pdfs.
#%pip install pytesseract pdf2image
import pytesseract

print(pytesseract.get_tesseract_version())
#this gave me an error.

#we found the issue. pytesseract is installed, but the Tesseract OCR engine itself is not installed on Windows.
#The official Tesseract documentation points Windows users to the UB Mannheim installers.
#Download the 64-bit Windows installer from:
#Tesseract Windows installers (UB Mannheim)
#Install it using the default location:
#C:\Program Files\Tesseract-OCR
#Close and reopen JupyterLab after installation.
#Run:
import pytesseract

print(pytesseract.get_tesseract_version())