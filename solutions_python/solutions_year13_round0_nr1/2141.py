#!/usr/bin/env python

import re

input_file = 'tictac-large.dat'

def test_position(board):
    empty_squares = False
    x_victory = False
    o_victory = False
    
    # Check for various outcomes...
    for row in board:
        x_row = re.sub('T', 'X', row)
        o_row = re.sub('T', 'O', row)
        
        if (x_row == 'XXXX'):
            x_victory = True
        elif (o_row == 'OOOO'):
            o_victory = True
        
        x_row = re.sub('O', 'X', x_row)
        if (x_row != 'XXXX'):
            empty_squares = True
    
    if (x_victory):
        return 1
    elif (o_victory):
        return 2
    elif (empty_squares):
        return 3
    else:
        return 4

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    
    for i in range(0, N_tests):
        board = []
        for j in range(0, 4):
            board.append(data_file.readline().strip())
        
        board_columns = []
        for j in range(0,4):
            col = ''
            for k in range(0,4):
                col += board[k][j]
            board_columns.append(col)
        
        board_diags = [
            board[0][0] + board[1][1] + board[2][2] + board[3][3],
            board[3][0] + board[2][1] + board[1][2] + board[0][3]
        ]
        
#        print board
#        print board_columns
#        print board_diags
        
        test_row = test_position(board)
        test_col = test_position(board_columns)
        test_diag = test_position(board_diags)
        
        cond_str = ""
        if (test_row == 1 or test_col == 1 or test_diag == 1):
            cond_str = "X won"
        elif (test_row == 2 or test_col == 2 or test_diag == 2):
            cond_str = "O won"
        elif (test_row == 3):
            cond_str = "Game has not completed"
        else:
            cond_str = "Draw"
        
        case_str = "Case #{0:d}: {1}".format(i+1, cond_str)
        print case_str
        
        data_file.readline()
        
