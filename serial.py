import cv2
import pytesseract
import numpy as np

img = cv2.imread('/home/pi/Pictures/serial2.jpg')
img = img[68:550,85:1340]
img = cv2.resize(img,(int(img.shape[1]*.5),int(img.shape[0]*.5)))

def readSerial(img):
    
    imgInverted = ~img
    imgGray = cv2.cvtColor(imgInverted, cv2.COLOR_BGR2GRAY)

    # 2 methods to read series number
    # OTSU
    ret2, th2 = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # OTSU after Gaussian Filtering
    blur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    # ###Detecting words
    boxes = pytesseract.image_to_data(th3)
    for x,b in enumerate(boxes.splitlines()):
        #
        print(b)
        if x != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                serial = b[len(b)-1]
                print('Serial = ',serial)
            



	return serial


