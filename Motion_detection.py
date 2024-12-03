import cv2
import imutils
import time
import numpy as np
address="http://10.139.33.126:8080/video"
cam = cv2.VideoCapture(address)
time.sleep(1)
fframe = None
area=500
while True:
   _,img = cam.read()
   text ="Normal"
   img = imutils.resize(img,width=500,height = 600)
   grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   gaussionImg = cv2.GaussianBlur(grayImg,(21,21),0)
   if fframe is None:
      fframe = gaussionImg
      continue
   ImgDiff=cv2.absdiff(fframe,gaussionImg)
   threshImg  = cv2.threshold(ImgDiff,25,255,cv2.THRESH_BINARY)[1]
   threshImg = cv2.dilate(threshImg,None, iterations=2)
   cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
   cnts = imutils.grab_contours(cnts)
   for c in cnts:
      if cv2.contourArea(c) < area:
         continue
      (x,y,w,h) = cv2.boundingRect(c)
      cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
      text = "Moving Object "
   print(text)
   cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
   cv2.imshow("cameraFeed", img)
   key = cv2.waitKey(1) & 0xFF
   if key == ord("q"):
      break
cam.release()
cv2.destroyAllWindows()
