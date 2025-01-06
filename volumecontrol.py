import cv2 as cv
import mediapipe as mp
import pyautogui as pg
from pynput.keyboard import Key,Controller

{
#
# cam = cv.VideoCapture(0)
# mphands = mp.solutions.hands
# hands = mphands.Hands()
# mpdraw = mp.solutions.drawing_utils
# index_y=0
# space = 0
# mykeys = Controller()
#
# while True:
#     _,img=cam.read()
#     img = cv.flip(img , 1)
#     frame_height,frame_width,_=img.shape
#     screen_width, screen_height=pg.size()
#     imgRGB=cv.cvtColor(img , cv.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
#     if results.multi_hand_landmarks:
#         for each in results.multi_hand_landmarks:
#             for id , lm in enumerate(each.landmark):
#                 h,w,c=img.shape
#                 cx,cy=int(lm.x*w),int(lm.y*h)
#
#                 if(id == 8):
#                     cv.circle(img,(cx,cy),7,(255,0,0),cv.FILLED)
#                     index_x = screen_width / frame_width * cx
#                     index_y = screen_height / frame_height * cy
#                     pg.moveTo(index_x, index_y)
#                 if (id == 4):
#                     cv.circle(img, (cx, cy), 7, (255, 0, 0), cv.FILLED)
#                     thumb_x = screen_width / frame_width * cx
#                     thumb_y = screen_height / frame_height * cy
#
#                     spacey=abs(index_y-thumb_y)
#                     spacex=abs(index_x-thumb_x)
#                 # print(space)
#                 if(spacey>300):
#                     mykeys.press(Key.media_volume_up)
#                 elif(spacey<100):
#                     mykeys.press(Key.media_volume_down)
#     cv.imshow('image',img)
#     cv.waitKey(1)
}
cam = cv.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
index_y = 0
space = 0
mykeys = Controller()

while True:
    _, img = cam.read()
    img = cv.flip(img, 1)
    frame_height, frame_width, _ = img.shape
    screen_width, screen_height = pg.size()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for each in results.multi_hand_landmarks:
            for id, lm in enumerate(each.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id,cx,cy)

                if (id == 8):
                    cv.circle(img, (cx, cy), 7, (0, 255, 255),cv.FILLED)
                    index_x = screen_width / frame_width * cx
                    index_y = screen_height / frame_height * cy
                    # pg.moveTo(index_x, index_y)
                if (id == 4):
                    cv.circle(img, (cx, cy), 7, (0, 255, 255),cv.FILLED)
                    thumb_x = screen_width / frame_width * cx
                    thumb_y = screen_height / frame_height * cy
                    # print(abs(index_y - thumb_y))
                    space = abs(index_y - thumb_y)
                    # gap = abs(index_x - thumb_x)


                # print(space)
                if (space > 250):
                    mykeys.press(Key.media_volume_up)
                    # mykeys.press(Key.)
                elif (space < 100):
                    mykeys.press(Key.media_volume_down)




    cv.imshow("image",img)
    cv.waitKey(1)
