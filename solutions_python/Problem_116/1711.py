'''
Created on Apr 12, 2013

@author: hou
'''

import sys
import re


def read_board(infile):
    board = []    
    for i in xrange(4):
        board.append(infile.readline().strip())
    
    infile.readline() # skip the empty line
    
    return board


def check_board(board, O_WIN, X_WIN):
    winner_r, empty_cell_r = check_row(board, O_WIN, X_WIN)
    winner_c, empty_cell_c = check_col(board, O_WIN, X_WIN)
    winner_d, empty_cell_d = check_diag(board, O_WIN, X_WIN)

    # get winner
    if winner_r:
        winner = winner_r
    elif winner_c:
        winner = winner_c
    elif winner_d:
        winner = winner_d
    else:
        winner = None
    
    # detect if contains empty cell
    empty_cell = empty_cell_r or empty_cell_c or empty_cell_d


    if not winner and not empty_cell:
        return 'Draw'
    elif not winner and empty_cell:
        return 'Game has not completed'
    elif winner and winner == 'O':
        return 'O won'
    elif winner and winner == 'X':
        return 'X won'


def check_row(board, O_WIN, X_WIN):
    winner = ""
    empty_cell = False
    for row in board:
        if '.' in row: 
            empty_cell = True
        elif O_WIN.match(row):
            winner = 'O'
        elif X_WIN.match(row):
            winner = 'X'
        
        if winner: break # stop as soon as got a winner
        
    return winner, empty_cell
     

def check_col(board, O_WIN, X_WIN):
    winner = ""
    empty_cell = False
    for i in xrange(4):
        col = board[0][i] + board[1][i] + board[2][i] + board[3][i]
        if '.' in col: 
            empty_cell = True
        elif O_WIN.match(col):
            winner = 'O'
        elif X_WIN.match(col):
            winner = 'X'
        
        if winner: break # stop as soon as got a winner
        
    return winner, empty_cell    


def check_diag(board, O_WIN, X_WIN):
    winner = ""
    empty_cell = False
    l_diag = []
    r_diag = []
    
    for i in xrange(4):
        l_diag.append(board[i][i])
        r_diag.append(board[i][3-i])
    l_diag = "".join(l_diag)
    r_diag = "".join(r_diag)
    
    if '.' in l_diag + r_diag: empty_cell = True
    
    if O_WIN.match(l_diag) or O_WIN.match(r_diag):
        winner = 'O'
    elif X_WIN.match(l_diag) or X_WIN.match(r_diag):
        winner = 'X'

    return winner, empty_cell


def main():
    O_WIN = re.compile('^[O, T]{4}$')
    X_WIN = re.compile('^[X, T]{4}$')
    

    infile = open(sys.argv[1])          # input file as the first arg
    outfile = open(sys.argv[2], 'w')    # output file as the second arg
    
    # get the number of test cases
    amount = int(infile.readline())
    
    # for each test case, determine the status
    for i in xrange(amount):
        board = read_board(infile)
        status = check_board(board, O_WIN, X_WIN)
        if status:
            outfile.write("Case #" + str(i+1) + ": " + status + '\n')
    
    # close files
    infile.close()
    outfile.close()  



if __name__=='__main__':
    main()
