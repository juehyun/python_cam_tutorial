import cv2
import datetime
import time

nCapture        = 30
timeIntervalSec = 0.5

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
#cap.set(3,10000)
#cap.set(4,10000)
w = int(cap.get(3))
h = int(cap.get(4))
print('width :%d, height : %d' % (w, h))

n=0
while(n<nCapture):
    ret, frame = cap.read()    # return and the image frame
    saveFileName = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-') + f'{n:02}.png'
    #print(f'{saveFileName}')
    #cv2.imshow('savePicture', frame)
    cv2.imwrite(saveFileName, frame)
    n=n+1
    time.sleep(timeIntervalSec)

cap.release()
cv2.destroyAllWindows()
