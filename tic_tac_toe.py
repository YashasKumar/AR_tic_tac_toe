import mediapipe as mp
import numpy as np
import cv2
import math

mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

cap=cv2.VideoCapture(0) 
start=False
x=np.zeros((3,3))
player_display = np.ones((480, 640, 3), dtype=np.uint8) * 255
turn=1

def make_lines(arr):
    cv2.line(arr, (230,200), (380, 200), (0,0,0), 2)
    cv2.line(arr, (230,250), (380, 250), (0,0,0), 2)
    cv2.line(arr, (280,150), (280, 300), (0,0,0), 2)
    cv2.line(arr, (330,150), (330, 300), (0,0,0), 2)
    return arr

def draw_turn(display, turn, x, y):#Used to display the XOX in the game box
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_thickness = 2
    font_color = (0, 0, 0)

    if turn == -1:
        cv2.putText(display, 'X', (x + 10, y + 36), font, font_scale, font_color, font_thickness, cv2.LINE_AA)
    else:
        cv2.putText(display, 'O', (x + 10, y + 36), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

def put_text_top(turn):
    if turn==-1:
        cv2.rectangle(player_display, (0, 0), (150, 30), (255, 255, 255), -1)  # Clear previous text
        cv2.putText(player_display, 'It is O\'s turn', (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_4)
    else:
        cv2.rectangle(player_display, (0, 0), (150, 30), (255, 255, 255), -1)  # Clear previous text
        cv2.putText(player_display, 'It is X\'s turn', (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_4)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        if cv2.waitKey(1)==ord('s'):#press letter s for a few seconds to start the game
            start=True
        ret, frame=cap.read()
        image = cv2.flip(frame, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image=make_lines(image)
        player_display=make_lines(player_display)
        landmarks = results.multi_hand_landmarks
        if landmarks:
            for num, hand in enumerate(landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1),
                                          mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)
                                          )
        if start:
            image_width, image_height = image.shape[1], image.shape[0]
            index = np.array([hand.landmark[8].x * image_width, hand.landmark[8].y * image_height])
            thumb = np.array([hand.landmark[4].x * image_width, hand.landmark[4].y * image_height])
            put_text_top(turn)

            distance = math.sqrt((index[0] - thumb[0])**2 + (index[1] - thumb[1])**2)
            
            if distance <= 20:#The distance between your index and thumb finger should be less than 20 pixels, basically touch them together in the box you want to place your character in
                if index[0]>=230 and index[0]<=280 and index[1]>=150 and index[1]<=200:
                    if x[0][0]==0:
                        if turn==1:
                            x[0][0]=1
                            turn=-1
                        else:
                            x[0][0]=-1
                            turn=1
                        draw_turn(player_display, turn, 230, 150)
                        put_text_top(turn)
                            
                if index[0]>=280 and index[0]<=330 and index[1]>=150 and index[1]<=200:
                    if x[0][1]==0:
                        if turn==1:
                            x[0][1]=1
                            turn=-1
                        else:
                            x[0][1]=-1
                            turn=1
                        draw_turn(player_display, turn, 280, 150)
                        put_text_top(turn)
                            
                if index[0]>=330 and index[0]<=380 and index[1]>=150 and index[1]<=200:
                    if x[0][2]==0:
                        if turn==1:
                            x[0][2]=1
                            turn=-1
                        else:
                            x[0][2]=-1
                            turn=1
                        draw_turn(player_display, turn, 330, 150)
                        put_text_top(turn)
                            
                if index[0]>=230 and index[0]<=280 and index[1]>=200 and index[1]<=250:
                    if x[1][0]==0:
                        if turn==1:
                            x[1][0]=1
                            turn=-1
                        else:
                            x[1][0]=-1
                            turn=1
                        draw_turn(player_display, turn, 230, 200)
                        put_text_top(turn)
                            
                if index[0]>=280 and index[0]<=330 and index[1]>=200 and index[1]<=250:
                    if x[1][1]==0:
                        if turn==1:
                            x[1][1]=1
                            turn=-1
                        else:
                            x[1][1]=-1
                            turn=1
                        draw_turn(player_display, turn, 280, 200)
                        put_text_top(turn)
                        
                if index[0]>=330 and index[0]<=380 and index[1]>=200 and index[1]<=250:
                    if x[1][2]==0:
                        if turn==1:
                            x[1][2]=1
                            turn=-1
                        else:
                            x[1][2]=-1
                            turn=1
                        draw_turn(player_display, turn, 330, 200)    
                        put_text_top(turn)
                        
                if index[0]>=230 and index[0]<=280 and index[1]>=250 and index[1]<=300:
                    if x[2][0]==0:
                        if turn==1:
                            x[2][0]=1
                            turn=-1
                        else:
                            x[2][0]=-1
                            turn=1
                        draw_turn(player_display, turn, 230, 250)
                        put_text_top(turn)
                        
                if index[0]>=280 and index[0]<=330 and index[1]>=250 and index[1]<=300:
                    if x[2][1]==0:
                        if turn==1:
                            x[2][1]=1
                            turn=-1
                        else:
                            x[2][1]=-1
                            turn=1
                        draw_turn(player_display, turn, 280, 250)
                        put_text_top(turn)
                                                            
                if index[0]>=330 and index[0]<=380 and index[1]>=250 and index[1]<=300:
                    if x[2][2]==0:
                        if turn==1:
                            x[2][2]=1
                            turn=-1
                        else:
                            x[2][2]=-1
                            turn=1
                        draw_turn(player_display, turn, 330, 250)
                        put_text_top(turn)
                            
                if x[0][0] == x[0][1] == x[0][2] == 1 or x[1][0] == x[1][1] == x[1][2] == 1 or x[2][0] == x[2][1] == x[2][2] == 1:
                    print("Congratulations! x has won the game")
                    break
                
                elif x[0][0] == x[1][0] == x[2][0] == 1 or x[0][1] == x[1][1] == x[2][1] == 1 or x[0][2] == x[1][2] == x[2][2] == 1:
                    print("Congratulations! x has won the game")
                    break
                
                elif x[0][0] == x[1][1] == x[2][2] == 1 or x[0][2] == x[1][1] == x[2][0] == 1:
                    print("Congratulations! x has won the game")
                    break
                    
                if x[0][0] == x[0][1] == x[0][2] == -1 or x[1][0] == x[1][1] == x[1][2] == -1 or x[2][0] == x[2][1] == x[2][2] == -1:
                    print("Congratulations! O has won the game")
                    break
                
                elif x[0][0] == x[1][0] == x[2][0] == -1 or x[0][1] == x[1][1] == x[2][1] == -1 or x[0][2] == x[1][2] == x[2][2] == -1:
                    print("Congratulations! O has won the game")
                    break
                
                elif x[0][0] == x[1][1] == x[2][2] == -1 or x[0][2] == x[1][1] == x[2][0] == -1:
                    print("Congratulations! O has won the game")
                    break
                
                elif np.count_nonzero(x == 0) == 0:
                    print("The game was a draw!")
                    break
               
        cv2.imshow('Camera', image)
        cv2.imshow('Game', player_display)
        if cv2.waitKey(1)== ord('q'):#Quit the game before it ends
            break
        
cap.release()
cv2.destroyAllWindows()