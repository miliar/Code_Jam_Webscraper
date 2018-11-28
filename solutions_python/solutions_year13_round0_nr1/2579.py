#!/usr/bin/python

import sys

fin = open(sys.argv[1])

def main():
    board = []
    i = 0
    firstline = True
    for line in fin.readlines():
        r = list(line.strip())
        if len(r) == 4 and not firstline:
            board += r
        if len(board) == 16:
            i += 1
            print "Case #"+str(i)+": "+check(board)
            board = []
        firstline = False

def check(board):
    xnum = toNum(board, 'X')
    onum= toNum(board, 'O')
    if checkNum(xnum):
        y = "X won"
    elif checkNum(onum):
        y = "O won"
    elif checkFull(board):
        y = "Draw"
    else:
        y = "Game has not completed"
    return y

def checkFull(board):
    i = 0
    for x in board:
        if x != '.':
            i += 1
    return i == 16

def toNum(board, c):
    s = ""
    for x in board:
        s += str(int(x==c or x=='T'))
    return int(s, 2)

def checkNum(i):
    return checkRow(i) or checkCol(i) or checkDiag(i)

def checkRow(i):
    return (i & 0xF000 == 0xF000) or (i & 0x0F00 == 0x0F00) or (i & 0x00F0 == 0x00F0) or (i & 0x000F == 0x000F)

def checkCol(i):
    return (i & 0x8888 == 0x8888) or (i & 0x4444 == 0x4444) or (i & 0x2222 == 0x2222) or (i & 0x1111 == 0x1111)

def checkDiag(i):
    return (i & 0x8421 == 0x8421) or (i & 0x1248 == 0x1248)

main()
