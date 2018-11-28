#!/usr/bin/env python3

import sys

cases = int (input ())

def Missing (board):
    for line in board:
        if '.' in line:
            return True

def wonDiagonal (player, board):
    # from 0, 0 to 3, 3
    won = True
    for i in range (4):
        if not won:
            break
        if board [i][i] != player:
            if board [i][i] != 'T':
                won = False
    if won: return True

    # from 3,0 to 0,3
    won = True
    for i in range (0, 4):
        if not won:
            break
        if board [3 - i][i] != player:
            if board [3 - i][i] != 'T':
                won = False
    if won: return True

    return False

def wonVertical (player, board):
    for column in range (4):
        col = [board [i][column] for i in range (4)]
        won = True
        print ("Checking if player", player, "won in column", col, file=sys.stderr)

        for row in col:
            if not won:
                break
            print ("\t", row, file=sys.stderr)
            if row != player:
                if row != 'T':
                    won = False

        if won:
            return True

    return False

def wonHorizontal (player, board):
    for line in board:
        won = True

        for block in line:
            if not won:
                break
            if block != player:
                if block != 'T':
                    won = False

        if won:
            return True

    return False

def won (player, board):
    if wonHorizontal (player, board):
        return True
    elif wonVertical (player, board):
        return True
    else:
        return wonDiagonal (player, board)

def XWon (board):
    return won ('X', board)

def OWon (board):
    return won ('O', board)

def answer():
    board = []
    for i in range (4):
        line = list (input ())
        board.append (line)
    print (board, file=sys.stderr)
    input ()

    if XWon (board):
        return "X won"
    elif OWon (board):
        return "O won"
    elif Missing(board):
        return "Game has not completed"
    else:
        return "Draw"

for i in range (cases):
    print ("Case #{0}: {1}".format (i + 1, answer ()))
