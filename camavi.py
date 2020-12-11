import cv2
import datetime

color  = True
width  = 1920
height = 1080

cam = cv2.VideoCapture(0) # 0 ~ 99
cam.set(3,width)
cam.set(4,height)
w = int(cam.get(3))
h = int(cam.get(4))
print('width :%d, height : %d' % (w, h))
print('quit  : q');
print('color : c');
print('gray  : g');

saveFileName = datetime.datetime.now().strftime('%Y%m%d-%H%M%S.avi')
fourcc       = cv2.VideoWriter_fourcc(*'DIVX')
out          = cv2.VideoWriter(saveFileName, fourcc, 25.0, (w, h))

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while(True):
    ret, frame = cam.read()
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

cam.release()
cv2.destroyAllWindows()

# Microsoft LifeCam Studio
# https://www.microsoft.com/accessories/en-us/business/lifecam-studio-for-business/5wh-00002#specsColumns-testCarousel
# 1080p image and moving picture(avi) (even the spec said 720p moving picture and 1080p image)

# cam.get(#)
#  0. CV_CAP_PROP_POS_MSEC      Current position of the video file in milliseconds.
#  1. CV_CAP_PROP_POS_FRAMES    0-based index of the frame to be decoded/captured next.
#  2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
#  3. CV_CAP_PROP_FRAME_WIDTH   Width of the frames in the video stream.
#  4. CV_CAP_PROP_FRAME_HEIGHT  Height of the frames in the video stream.
#  5. CV_CAP_PROP_FPS           Frame rate.
#  6. CV_CAP_PROP_FOURCC        4-character code of codec.
#  7. CV_CAP_PROP_FRAME_COUNT   Number of frames in the video file.
#  8. CV_CAP_PROP_FORMAT        Format of the Mat objects returned by retrieve() .
#  9. CV_CAP_PROP_MODE          Backend-specific value indicating the current capture mode.
# 10. CV_CAP_PROP_BRIGHTNESS    Brightness of the image (only for cameras).
# 11. CV_CAP_PROP_CONTRAST      Contrast of the image (only for cameras).
# 12. CV_CAP_PROP_SATURATION    Saturation of the image (only for cameras).
# 13. CV_CAP_PROP_HUE           Hue of the image (only for cameras).
# 14. CV_CAP_PROP_GAIN          Gain of the image (only for cameras).
# 15. CV_CAP_PROP_EXPOSURE      Exposure (only for cameras).
# 16. CV_CAP_PROP_CONVERT_RGB   Boolean flags indicating whether images should be converted to RGB.
# 17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
# 18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
