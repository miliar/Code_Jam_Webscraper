#!/usr/bin/python

import sys

def format_test_case(i, outcome):
    return "Case #%i: %s" % (i+1, outcome)

def load_board(stdin):
    board = []
    for i in xrange(4):
        row = list(stdin.readline().strip())
        board.append(row)
    return board

#outcomes
XW = "X won"
OW = "O won"
NC = "Game has not completed"
DRAW  = "Draw"

def check(moves):
    if '.' in moves:
        return NC
    if 'X' in moves and 'O' in moves:
        return DRAW
    if 'X' in moves:
        return XW
    if 'O' in moves:
        return OW

def find_guesses(board):
    guesses = []
    for row in board:
        guesses.append(check(row))
    for i in xrange(4):
        col = map(lambda row: row[i], board)
        guesses.append(check(col))
    diag_0 = map(lambda x: x[1][x[0]], enumerate(board))
    guesses.append(check(diag_0))
    diag_1 = map(lambda x: x[1][3 - x[0]], enumerate(board))
    guesses.append(check(diag_1))
    return guesses

def find_outcome(board):
    guesses = find_guesses(board)
    best_guess = None
    for guess in guesses:
        if guess in [XW, OW]:
            return guess
        if guess == NC:
            best_guess = NC
        elif guess == DRAW and best_guess != NC:
            best_guess = DRAW
    return best_guess

if __name__=='__main__':
    T = int(sys.stdin.readline())
    for i in xrange(T):
        board = load_board(sys.stdin)
        print format_test_case(i, find_outcome(board))
        sys.stdin.readline() # skip empty line
