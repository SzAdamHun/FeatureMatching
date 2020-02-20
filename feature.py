import cv2
import numpy as np
# from matplotlib import pyplot as plt

# Initialize
cap = cv2.VideoCapture('driving.mp4')
orb = cv2.ORB()

# Loop
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    o = cv2.ORB_create()
    kp = o.detect(frame, None)
    
    img2 = cv2.drawKeypoints(frame, kp, outImage = None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('frame', img2)
    
    cv2.waitKey(1)
   # if cv2.waitKey(0) and 0xFF == ord('q'):
   #     break


cap.release()
cv2.destroyAllWindows()
