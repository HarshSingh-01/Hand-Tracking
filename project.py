import cv2
import mediapipe as mp
import time
import handTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True: 
    # Reading the frame
    success, img = cap.read()
    # Converting Image from BGR to RGB
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    # if len(lmList) != 0:
        # print(lmList)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break

