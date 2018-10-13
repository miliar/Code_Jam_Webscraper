#!/usr/bin/python

from math import *

def find(board, p):
    pos = [p, 'T']
    for i in range(4):
        counterH, counterV = 0, 0
        for j in range(4):
            if board[i][j] in pos:
                counterH += 1
            else:
                counterH = 0
            if board[j][i] in pos:
                counterV += 1
            else:
                counterV = 0
            if counterH==4 or counterV==4:
                return True
            if (3-j+counterH<4) and (3-j+counterV<4):
                break
    
    c1 = 4
    c2 = 4
    for i in range(4):
        if board[i][i] in pos:
            c1 -= 1
        else:
            c1 = 4
        if board[i][3-i] in pos:
            c2 -= 1
        else:
            c2 = 4
    return not c1 or not c2
    
def hasDot(board):
    dot = '.'
    for row in board:
        if dot in row:
            return True
    return False

def checkBoard(board):
    x = find(board, 'X')
    o = find(board, 'O')
    if x and o:
        return "Draw"
    if x:
        return "X won"
    elif o:
        return "O won"
    elif hasDot(board):
        return "Game has not completed"
    else:
        return "Draw"
    

def readBoard():
    board = []
    for i in range(4):
        board.append(list(raw_input()))
    return board

boards=[]

T = int(raw_input())
for i in range(1, T+1):
    board = readBoard()
    #boards.append(board)
    print "Case #%d: %s"%(i, checkBoard(board))
    raw_input()

def stress():
    for board in boards*177:
        T+=1
        print T, checkBoard(board)
#stress()
