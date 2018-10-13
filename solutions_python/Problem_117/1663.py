'''
Created on 13. apr. 2013

@author: jont
'''

from sys import stdin

number_of_test_cases = int(stdin.readline())


def check_board(board):
    rows = len(board)
    cols = len(board[0])
    boardT = zip(*board)
    
    for i in range(rows):
        max_in_row = max(board[i])
        for j in range(cols):
            if board[i][j] != max_in_row:
                if board[i][j] != max(boardT[j]):
                    return "NO"
    
    
    for j in range(cols):
        max_in_col = max(boardT[j])
        for i in range(rows):
            if board[i][j] != max_in_col:
                if board[i][j] != max(board[i]):
                    return "NO"
    
    # If nothing yet
    return "YES"


for case in range(1, number_of_test_cases + 1):
    board = []
    rows, cols = stdin.readline().split()
    rows, cols = int(rows), int(cols)
    for i in range(rows):
        board.append(stdin.readline().split())
    
    print("Case #" + str(case) + ": " + check_board(board))