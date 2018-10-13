'''
Created on 13. apr. 2013

@author: jont
'''

from sys import stdin

number_of_test_cases = int(stdin.readline())

def check_status(board):
    for player in ["X", "O"]:
        # Check all rows
        for row in range(4):
            winner = True
            for col in range(4):
                if board[row][col] != player and board[row][col] != "T":
                    winner = False
            if winner == True:
                return player + " won"
        
        # Check all cols 
        for col in range(4):
            winner = True
            for row in range(4):
                if board[row][col] != player and board[row][col] != "T":
                    winner = False
            if winner == True:
                return player + " won"
            
        # Check top-left to bottom-left diagonal
        winner = True
        for i in range(4):
            if board[i][i] != player and board[i][i] != "T":
                winner = False
        if winner == True:
            return player + " won"
        
        # Check top-right to bottom-right diagonal
        winner = True
        for i in range(4):
            if board[i][3-i] != player and board[i][3-i] != "T":
                winner = False
        if winner == True:
            return player + " won" 
        
    # If no of the players has won
    # Check if game is finished -> Draw
    draw = True
    for row in range(4):
        for col in range(4):
            if board[row][col] == ".":
                draw = False
    if draw == True:
        return "Draw"
    else:
        return "Game has not completed"
    
    # Should not come to this
    return "Something went wrong"


for case in range(1, number_of_test_cases + 1):
    board = []
    for i in range(4):
        board.append([])
        for s in stdin.readline():
            board[i].append(s)
    
    print("Case #" + str(case) + ": " + check_status(board))
    
    if i < number_of_test_cases - 1:
        stdin.readline() # Blank line