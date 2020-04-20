import cv2
cv2.__version__ #using opencv version 4.2.0

import imutils # imutils module contains convenience functions for resizing, rotating, and cropping images.
from skimage.filters import threshold_local #the threshold_local function from scikit-imagefunction which will help us obtain the “black and white” feel to our scanned image.

from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract # OCR image
import re # Using regular expressions to determine emails or phone numbers

img = cv2.imread('image.jpg')
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
ratio = img.shape[0] / 500.0
orig = img.copy()
img = imutils.resize(img, height = 500) #500 pixels

#convert image to grayscale, blur it and find edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0) #Remove high-frequency noise
edged = cv2.Canny (gray, 75, 200) # Canny Edge Detection

#show original and edge detected image
cv2.imshow ("Image", img)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()