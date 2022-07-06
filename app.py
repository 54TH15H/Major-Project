from tkinter import *
import pyautogui
import numpy as np
import HandTracking as ht
import cv2
import time
import autopy

def fun():
    global text
    text.insert(END, "Wait a minute, All the packages are getting ready.\n")
    pTime = 0
    wid = 640
    hei = 480
    frameR = 100
    smoothening = 8
    prev_x, prev_y = 0, 0
    curr_x, curr_y = 0, 0

    cap = cv2.VideoCapture(0)
    cap.set(3, wid)
    cap.set(4, hei)

    detector = ht.handDetector(maxHands=2)
    screen_width, screen_height = autopy.screen.size()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist, bbox = detector.findPosition(img)
        if len(lmlist) != 0:
            text.insert(END, "Hand Opened.\n")
            x1, y1 = lmlist[8][1:]
            x2, y2 = lmlist[12][1:]

            fingers = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (wid - frameR, hei - frameR), (255, 0, 255),2)
            if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
                text.insert(END, "Mouse moving....({},{})\n".format(prev_x,prev_y))
                x3 = np.interp(x1, (frameR, wid - frameR), (0, screen_width))
                y3 = np.interp(y1, (frameR, hei - frameR), (0, screen_height))

                curr_x = prev_x + (x3 - prev_x) / smoothening
                curr_y = prev_y + (y3 - prev_y) / smoothening

                autopy.mouse.move(screen_width - curr_x, curr_y)
                cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y

            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
                x3 = np.interp(x1, (frameR, wid - frameR), (0, screen_width))
                y3 = np.interp(y1, (frameR, hei - frameR), (0, screen_height))

                curr_x = prev_x + (x3 - prev_x) / smoothening
                curr_y = prev_y + (y3 - prev_y) / smoothening

                autopy.mouse.move(screen_width - curr_x, curr_y)
                cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y
                text.insert(END, "Ready to Click.\n")
                length, img, lineInfo = detector.findDistance(8, 12, img)

                if length < 40:
                    text.insert(END, "Single Clicked.\n")
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
            if fingers == [1, 1, 1, 0, 0]:
                pyautogui.mouseDown(button='right')
                text.insert(END, "Right Clicking.\n")
            if fingers == [0, 1, 1, 1, 0]:
                # pyautogui.mouseDown(button='left')
                text.insert(END, "Left Clicking.\n")
            if fingers == [0, 0, 0, 0, 1]:
                # pyautogui.scroll(10, _pause=False)
                text.insert(END, "Scrolling Down.\n")
            if fingers == [1, 0, 0, 0, 0]:
                # pyautogui.scroll(-10, _pause=True)
                text.insert(END, "Scrolling Up.\n")

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Video Output", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return
def close(): exit(0)
def keybd():
    pTime = 0
    wid = 1280
    hei = 960
    frameR = 100
    smoothening = 8
    prev_x, prev_y = 0, 0
    curr_x, curr_y = 0, 0

    cap = cv2.VideoCapture(0)
    cap.set(3, wid)
    cap.set(4, hei)
    inp = ""
    detector = ht.handDetector(maxHands=2)
    screen_width, screen_height = autopy.screen.size()

    kb = [list(map(str, '1 2 3 4 5 6 7 8 9 0'.split(' '))), list(map(str, 'Q W E R T Y U I O P '.split(' '))),
          list(map(str, 'A S D F G H J K L ;'.split(' '))),
          list(map(str, 'Z X C V B N M < > <-'.split(' '))), list(map(str, '! @ # $ SPACE ; & * ( CLS'.split(' ')))]
    kby = [380, 413, 449, 483, 518, 551]

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        cv2.namedWindow("Video Output")
        lmlist, bbox = detector.findPosition(img)
        cv2.moveWindow("Video Output", 0, 0)
        cv2.putText(img, inp, (60, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        # if cv2.waitKey(1) & 0xFF == ord('w'):
        #     print(f'({pyautogui.position().x-300},{pyautogui.position().y-190})')

        if len(lmlist) != 0:
            x1, y1 = lmlist[8][1:]
            x2, y2 = lmlist[12][1:]

            fingers = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (wid - frameR, hei - frameR), (255, 0, 255), 2)
            if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
                x3 = np.interp(x1, (frameR, wid - frameR), (0, screen_width))
                y3 = np.interp(y1, (frameR, hei - frameR), (0, screen_height))

                curr_x = prev_x + (x3 - prev_x) / smoothening
                curr_y = prev_y + (y3 - prev_y) / smoothening

                autopy.mouse.move(screen_width - curr_x, curr_y)
                cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y

            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
                x3 = np.interp(x1, (frameR, wid - frameR), (0, screen_width))
                y3 = np.interp(y1, (frameR, hei - frameR), (0, screen_height))

                curr_x = prev_x + (x3 - prev_x) / smoothening
                curr_y = prev_y + (y3 - prev_y) / smoothening

                autopy.mouse.move(screen_width - curr_x, curr_y)
                cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y

                length, img, lineInfo = detector.findDistance(8, 12, img)

                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()

                    # -------- keyboard clicks -----------

                    tkb = 0
                    for kbxy in range(5):
                        if pyautogui.position().x - 300 >= -278 and pyautogui.position().x - 300 <= -154 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][0]
                        elif pyautogui.position().x - 300 >= -154 and pyautogui.position().x - 300 <= -29 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][1]
                        elif pyautogui.position().x - 300 >= -29 and pyautogui.position().x - 300 <= 97 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][2]
                        elif pyautogui.position().x - 300 >= 97 and pyautogui.position().x - 300 <= 221 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][3]
                        elif pyautogui.position().x - 300 >= 221 and pyautogui.position().x - 300 <= 346 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            if kbxy == 4:
                                inp += " "
                            else:
                                inp += kb[kbxy][4]
                        elif pyautogui.position().x - 300 >= 346 and pyautogui.position().x - 300 <= 472 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            if kbxy == 4:
                                inp += " "
                            else:
                                inp += kb[kbxy][5]
                        elif pyautogui.position().x - 300 >= 472 and pyautogui.position().x - 300 <= 596 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][6]
                        elif pyautogui.position().x - 300 >= 596 and pyautogui.position().x - 300 <= 720 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][7]
                        elif pyautogui.position().x - 300 >= 720 and pyautogui.position().x - 300 <= 847 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            inp += kb[kbxy][8]
                        elif pyautogui.position().x - 300 >= 847 and pyautogui.position().x - 300 <= 968 and pyautogui.position().y - 190 >= \
                                kby[kbxy] and pyautogui.position().y - 190 <= kby[kbxy + 1]:
                            if kbxy == 3:
                                inp = inp[:-1]
                            elif kbxy == 4:
                                inp = ""
                            else:
                                inp += kb[kbxy][9]

            if fingers == [1, 1, 1, 0, 0]:
                pyautogui.mouseDown(button='right')
            if fingers == [0, 1, 1, 1, 0]:
                pyautogui.mouseDown(button='left')
            if fingers == [0, 0, 0, 0, 1]:
                pyautogui.scroll(10, _pause=False)
            if fingers == [1, 0, 0, 0, 0]:
                pyautogui.scroll(-10, _pause=True)

        # -------- keyboard -----------

        cv2.rectangle(img, (10, 525), (1260, 700), (100, 100, 100), -1)

        cv2.line(img, (10, 525), (1260, 525), (255, 255, 255), 1)
        cv2.line(img, (10, 560), (1260, 560), (255, 255, 255), 1)
        cv2.line(img, (10, 595), (1260, 595), (255, 255, 255), 1)
        cv2.line(img, (10, 630), (1260, 630), (255, 255, 255), 1)
        cv2.line(img, (10, 665), (1260, 665), (255, 255, 255), 1)
        cv2.line(img, (10, 700), (1260, 700), (255, 255, 255), 1)

        cv2.line(img, (10, 525), (10, 700), (255, 255, 255), 5)
        cv2.line(img, (135, 525), (135, 700), (255, 255, 255), 5)
        cv2.line(img, (260, 525), (260, 700), (255, 255, 255), 5)
        cv2.line(img, (385, 525), (385, 700), (255, 255, 255), 5)
        cv2.line(img, (510, 525), (510, 700), (255, 255, 255), 5)
        cv2.line(img, (635, 525), (635, 665), (255, 255, 255), 5)  # 700
        cv2.line(img, (760, 525), (760, 700), (255, 255, 255), 5)
        cv2.line(img, (885, 525), (885, 700), (255, 255, 255), 5)
        cv2.line(img, (1010, 525), (1010, 700), (255, 255, 255), 5)
        cv2.line(img, (1135, 525), (1135, 700), (255, 255, 255), 5)
        cv2.line(img, (1260, 525), (1260, 700), (255, 255, 255), 5)

        # ------- Keyboard Keys --------

        ky, thickness = 555, 3
        for i in range(5):
            cv2.putText(img, kb[i][0], (60, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][1], (180, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][2], (310, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][3], (440, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][4], (570, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][5], (690, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][6], (810, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][7], (940, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][8], (1060, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            cv2.putText(img, kb[i][9], (1180, ky), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness)
            ky += 35

        # -------- keyboard keys -----------

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Video Output", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return

def mainn():
    global text
    main = Tk()
    main.geometry("450x300")

    font = ('times', 16, 'bold')
    title = Label(main, text='Virtual Mouse and Keyboard Using Hand Gestures')
    title.config(bg='dark salmon', fg='black')
    title.config(font=font)
    title.config(height=3, width=120)
    title.place(x=0,y=5)

    font1 = ('times', 14, 'bold')
    text = Text(main, height=30, width=80)
    download = Button(main, text="VIRTUAL MOUSE",activebackground="green", activeforeground="white", command=fun)
    download.place(x=700,y=100)
    download.config(font=font1)

    cvect = Button(main, text="VIRTUAL KEYBOARD",activebackground="green", activeforeground="white", command=keybd)
    cvect.place(x=700,y=150)
    cvect.config(font=font1)
    tfvect = Button(main, text="CLOSE",activebackground="green", activeforeground="white", command=close)
    tfvect.place(x=700,y=200)
    tfvect.config(font=font1)
    font1 = ('times', 12, 'bold')
    scroll=Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.insert(END,"Wait a minute, Packages are loading....\n")
    text.place(x=10,y=100)
    text.config(font=font1)
    main.config(bg='ivory2')
    main.mainloop()

mainn()