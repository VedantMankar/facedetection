import cv2
import numpy as np

#loading two cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#loading webcam
cap = cv2.VideoCapture(0)

while True:
	ret,img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,5)
	#x,y width,height in faces
	for(x,y,w,h) in faces:
		#drawing a rectangle on img
		#2nd and 3rd argument are start and end point of  rectangle,then we give blue color with a linewidth of 2
		cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h,x:x+w]
		roi_color =img[y:y+h,x:x+w]
		#now detecting eye
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()