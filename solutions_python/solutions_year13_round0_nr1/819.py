'''
Created on 2013/04/13

@author: hanaue51
'''

import os
os.chdir("../../../data/2013/qualification/")
filename = "A-large"
postfix_in = ".in"
postfix_out = ".out"

def has_won(board, player):
    row_filled = [True for i in xrange(len(board))]
    col_filled = [True for i in xrange(len(board))]
    diag_filled = [True, True]
    
    for row in xrange(len(board)):
        for col in xrange(len(board)):
            if board[row][col] != 'T' and board[row][col] != player:
                row_filled[row] = False
                col_filled[col] = False
                if row == col:
                    diag_filled[0] = False
                elif row + col == len(board) - 1:
                    diag_filled[1] = False
    
    return (row_filled.count(True) + col_filled.count(True) + diag_filled.count(True) > 0)

def tic_tac_toe_tomek_status(board):
    result = "Game has not completed"
    
    # (1) X -> O -> X -> O ...
    # # of chars: (1-1) even => O may have won, (1-2) odd => X may have won
    # (2) T -> X -> O -> X -> O ...
    # # of chars: (2-1) even => X may wave won, (2-2) odd => O may have won
    count_T = 0
    count_empty = 0
    for line in board:
        count_T += line.count('T');
        count_empty += line.count('.')
    
    if count_empty == 0:
        result = "Draw"
    
    if count_T % 2 == 0:
        # case (1)
        if count_empty % 2 == 0:
            # case (1-1) O may have won
            if has_won(board, "O"):
                result = "O won"
        else:
            # case (1-2) X may have won
            if has_won(board, "X"):
                result = "X won"
    else:
        # case (2)
        if count_empty % 2 == 0:
            # case (2-1) X may have won
            if has_won(board, "X"):
                result = "X won"
        else:
            # case (2-2) O may have won
            if has_won(board, "O"):
                result = "O won"
    
    return result

results = []
format = "Case #%d: %s\n"

# read inputs
infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

cases_count = int(lines[0].strip())
first = 1
lines_per_board = 4
for i in xrange(cases_count):
    board = lines[first:first+lines_per_board]
    if len(board) == lines_per_board:
        results.append(format % (i + 1, tic_tac_toe_tomek_status(board)))
    first += lines_per_board + 1

# write results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
    outfile.write(result)
outfile.close()
