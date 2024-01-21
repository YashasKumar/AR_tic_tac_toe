# AR_tic_tac_toe
This is a small piece of code made using mediapipe and opencv, which enables users to play an AR tic tac toe game using hand gestures

Overview
This Python script implements a unique twist to the classic Tic-Tac-Toe game by allowing players to make moves using hand gestures captured through a webcam. The game utilizes the MediaPipe library for hand tracking, providing an interactive and fun way to play Tic-Tac-Toe.

Features
Hand Tracking: Utilizes the MediaPipe library to track hand movements in real-time.
Interactive Gameplay: Players make moves by placing 'X' or 'O' on the Tic-Tac-Toe grid using hand gestures.
Visual Feedback: Displays live camera feed, the Tic-Tac-Toe board, and turn information for an engaging user experience.

Prerequisites
Python 3.x
OpenCV
NumPy
MediaPipe

Installation
Clone the repository:
git clone https://github.com/yourusername/hand-gesture-tic-tac-toe.git
cd hand-gesture-tic-tac-toe
Install the required libraries:
pip install opencv-python numpy mediapipe
How to Play
Run the script:
python tic_tac_toe.py

Press the 's' key to start the game. The camera feed and Tic-Tac-Toe board will be displayed.
Make hand gestures to place 'X' or 'O' in the Tic-Tac-Toe grid.
To quit the game, press the 'q' key.

Hand Gestures
The distance between the index and thumb fingers should be less than 20 pixels to place a character on the grid, basically your index and thumb should be touching each other inside the box you want to place your character in.

Game Rules
Players take turns placing their symbol ('X' or 'O') on the board.
The game announces the winner when a player gets three in a row horizontally, vertically, or diagonally.
The game declares a draw when the board is full, and no player has won.

Acknowledgments
This project was inspired by the combination of hand tracking technology and the classic Tic-Tac-Toe game.
Feel free to modify, enhance, and share this code!
