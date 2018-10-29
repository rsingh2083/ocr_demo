import cv2
import numpy as np
import os
print("PRESS 'q' to exit")
print("PRESS 's' to select region of interest")
cap = cv2.VideoCapture(0)

while(True):
	_, frame = cap.read()

	convert = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	#cv2.imshow("orignal", frame)
	cv2.imshow("orignal", convert)

	key = cv2.waitKey(1) & 0xFF
	if(key == ord('q')):
		break
	elif(key == ord('s')):
		cv2.imwrite('tp.jpg', frame)
		r = cv2.selectROI(convert)
	 	# Crop image
		imCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
	 	 # Display cropped image
		cv2.imshow("Image", imCrop)
		cv2.imwrite("image.jpg",imCrop)
		cv2.destroyWindow("Image")
		cv2.destroyWindow("ROI selector")
		os.system('python3 img2text.py image.jpg')
cv2.destroyAllWindows()
