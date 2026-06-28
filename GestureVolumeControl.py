import cv2
import time
import numpy as np
import math
from HandTrackingModule import HandDetector
from pycaw.pycaw import AudioUtilities

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume

minVol = volume.GetVolumeRange()[0]
maxVol = volume.GetVolumeRange()[1]

wcam, hcam = 800, 500

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

ptime = 0
Detector = HandDetector()

vol = 0
volBar = 400
volPer = 0

while True:

    success, img = cap.read()
    if not success:
        break

    ctime = time.time()
    fps = 0 if ptime == 0 else 1 / (ctime - ptime)
    ptime = ctime

    img = Detector.findHands(img)
    lmlist = Detector.findPosition(img)

    if len(lmlist) != 0:

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        length = math.hypot(x2 - x1, y2 - y1)

        cv2.circle(img, (x1, y1), 8, (10, 10, 200), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (10, 10, 200), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (10, 10, 200), 3)
        cv2.circle(img, (cx, cy), 8, (10, 10, 200), cv2.FILLED)

        if length < 50:
            cv2.circle(img, (cx, cy), 8, (0, 255, 0), cv2.FILLED)

        length = max(50, min(length, 250))

        vol = np.interp(length, [50, 250], [minVol, maxVol])
        volBar = np.interp(length, [50, 250], [400, 100])
        volPer = np.interp(length, [50, 250], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)

    cv2.rectangle(img, (40, 100), (70, 400), (250, 15, 40), 4)
    cv2.rectangle(img, (40, int(volBar)), (70, 400), (250, 15, 40), cv2.FILLED)
    cv2.putText(img, f"{int(volPer)}%", (30, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 15, 40), 2)
    cv2.putText(img, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (51, 55, 0), 2)

    cv2.imshow("Volume Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()