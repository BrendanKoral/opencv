import cv2
import numpy as np

#Captures from first webcam input
cap = cv2.VideoCapture(0)

#Selects XVID encoding
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Writes output, names file, chooses dimensions
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#Keeps webcam open until Q is pressed, then closes all windows
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('frame',frame)
	cv2.imshow('gray', gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()