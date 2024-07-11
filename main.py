import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
finger_tips = [8, 12, 16, 20]
thumb_tip = 4
index_finger_tip = 8
middle_finger_tip = 12

if not cap.isOpened():
    print("Error: Could not open camera. Switching to fallback mode...")
    # Use a fallback image or video
    img = cv2.imread("images/fallback_image.png")
else:
    ret, img = cap.read()
    if not ret:
        print("Error: Failed to capture image from camera.")
        img = None

# Process the image or fallback content
if img is not None:
    # Your image processing logic here
    cv2.imshow("Processed Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: No image data available.")

# reading image from opencv
like_img = cv2.imread("images/like.jpg")
like_img = cv2.resize(like_img, (200, 180))

dislike_img = cv2.imread("images/dislike.jpg")
dislike_img = cv2.resize(dislike_img, (200, 180))

victory_img = cv2.imread("images/victory.jpg")
victory_img = cv2.resize(victory_img, (200, 180))

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            finger_fold_status = []
            for tip in finger_tips:
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                print(id, ":", x, y)
                cv2.circle(img, (x,  y), 15, (255, 0, 0), cv2.FILLED)

                if lm_list[tip].x < lm_list[tip - 3].x:
                    cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)

            print(finger_fold_status)

            x,y = int(lm_list[8].x*w),int(lm_list[8].y*h)
            print(x,y)
            #a
            if  lm_list[4].y<lm_list[2].y and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and  \
                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "A", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("A")
            #b
            elif lm_list[4].y<lm_list[1].y  and lm_list[8].y<lm_list[6].y and lm_list[12].y<lm_list[10].y and \
                lm_list[16].y<lm_list[14].y and lm_list[20].y<lm_list[18].y and lm_list[17].x<lm_list[0].x< \
                lm_list[5].x:
                cv2.putText(img,"B",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("B")
            #d
            elif  lm_list[4].y<lm_list[1].y and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and  \
                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "D", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("D")
            #F
            elif lm_list[4].y<lm_list[2].y  and lm_list[8].y>lm_list[6].y and lm_list[12].y<lm_list[10].y and \
                 lm_list[16].y<lm_list[14].y and lm_list[20].y<lm_list[18].y and lm_list[17].x<lm_list[0].x< \
                 lm_list[5].x:
                cv2.putText(img,"F",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("F")
            #M
            elif lm_list[3].x > lm_list[4].x and\
                 lm_list[8].y > lm_list[7].y > lm_list[6].y and lm_list[12].y > lm_list[11].y > lm_list[10].y and\
                 lm_list[16].y > lm_list[15].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "M", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("M")

            #W
            elif lm_list[3].x > lm_list[4].x  and lm_list[8].y<lm_list[6].y and lm_list[12].y<lm_list[10].y and \
                lm_list[16].y<lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img,"W",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("W")
            #Y
            elif lm_list[4].y<lm_list[2].y and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and  \
                lm_list[16].y > lm_list[14].y and lm_list[20].y<lm_list[18].y and lm_list[17].x<lm_list[0].x< \
                lm_list[5].x:
                cv2.putText(img, "Y", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Y")
            #ekdum op
            elif lm_list[3].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x< \
                lm_list[5].x:
                cv2.putText(img,"Fabulous",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("Fabulous")
            # Victory
            elif lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "VICTORY, V", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("VICTORY, V")

            #Forward
            elif lm_list[3].x>lm_list[4].x and lm_list[8].y<lm_list[6].y and lm_list[12].y>lm_list[10].y and \
                lm_list[16].y>lm_list[14].y and lm_list[20].y>lm_list[18].y:
                cv2.putText(img,"FORWARD",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("FORWARD")

            #Backward
            elif lm_list[3].x>lm_list[4].x and lm_list[3].y<lm_list[4].y and lm_list[8].y>lm_list[6].y and \
                lm_list[12].y<lm_list[10].y and lm_list[16].y<lm_list[14].y and lm_list[20].y<lm_list[18].y:
                cv2.putText(img,"BACKWARD",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("BACKWARD")

            #Left
            elif lm_list[4].y<lm_list[2].y and lm_list[8].x<lm_list[6].x and lm_list[12].x>lm_list[10].x and \
                lm_list[16].x>lm_list[14].x and lm_list[20].x>lm_list[18].x and lm_list[5].x<lm_list[0].x:
                cv2.putText(img,"LEFT",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("LEFT")

            #Right
            elif lm_list[4].y<lm_list[2].y and lm_list[8].x>lm_list[6].x and lm_list[12].x<lm_list[10].x and \
                lm_list[16].x<lm_list[14].x and lm_list[20].x<lm_list[18].x:
                cv2.putText(img,"RIGHT",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("RIGHT")

            if all(finger_fold_status):
                # like
                if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y:
                    print("Good")
                    cv2.putText(img, "GOOD", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    h, w, c = like_img.shape
                    img[35:h + 35, 30:w + 30] = like_img
                # Dislike
                elif lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y:
                    cv2.putText(img, "BAD", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    print("Bad")
                    h, w, c = dislike_img.shape
                    img[35:h + 35, 30:w + 30] = dislike_img
                #

            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                   mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                   ) # accessing hand connections object,and choosing color, thickness ,radius

    cv2.imshow("Hand Gesture Detection", img)
    cv2.waitKey(1)

'''
 #stop
            if lm_list[4].y<lm_list[2].y and lm_list[8].y<lm_list[6].y and lm_list[12].y<lm_list[10].y and \
                lm_list[16].y<lm_list[14].y and lm_list[20].y<lm_list[18].y and lm_list[17].x<lm_list[0].x< \
                lm_list[5].x:
                cv2.putText(img,"STOP, 5",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                print("STOP, 5")
'''