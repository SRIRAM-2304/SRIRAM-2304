import cv2
import time
import imutils

alg = "haarcascade_frontalface_default.xml"
haarcascade = cv2.CascadeClassifier(alg)
address = "http://10.139.33.126:8080/video"
cam = cv2.VideoCapture(address)
time.sleep(1)

while True:
    ret, img = cam.read()
    if not ret:
        break
    
    img = imutils.resize(img, width=1000)
    grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    face = haarcascade.detectMultiScale(grayImg, 1.3, 4)
    
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("FaceDetect", img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
