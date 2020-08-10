import cv2
import datetime

color = True

cap = cv2.VideoCapture(0)
#cap.set(3,10000)
#cap.set(4,10000)
cap.set(3,1920)
cap.set(4,1080)
w = int(cap.get(3))
h = int(cap.get(4))
print('width :%d, height : %d' % (w, h))
print('quit  : q');
print('color : c');
print('gray  : g');

saveFileName = datetime.datetime.now().strftime('%Y%m%d-%H%M%S.avi')
fourcc       = cv2.VideoWriter_fourcc(*'DIVX')
out          = cv2.VideoWriter(saveFileName, fourcc, 25.0, (w, h))

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while(True):
    ret, frame = cap.read()
    if(ret):
        if(color):
            cv2.imshow('frame', frame)
            out.write(frame)
        else:
            gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY) # convert to gray(1ch)
            gfrm = cv2.cvtColor(gray ,  cv2.COLOR_GRAY2BGR) # re-convert to 3ch (remain gray)
            cv2.imshow('frame', gfrm)
            out.write(gfrm)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('c'):
            color = True
            print('set color mode : True')
        elif key == ord('g'):
            color = False
            print('set color mode : False')

cap.release()
cv2.destroyAllWindows()
