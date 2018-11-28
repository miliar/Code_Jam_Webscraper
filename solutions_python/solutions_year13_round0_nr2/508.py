#!/usr/bin/python

from math import *

def checkBoard(board, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j]!=2:
                if 1 not in [ board[0][j], board[n-1][j], board[i][0], board[i][m-1] ]:
                    return False
    return True
    
def checkBoard2(board, n, m):
    maxr = [max(v) for v in board]
    cols = [[board[i][j] for i in range(len(board))] for j in range(len(board[0]))]
    maxc = [max(x) for x in cols]
    for i in range(n):
        for j in range(m):
            v = board[i][j] 
            if v != maxr[i] and v != maxc[j]:
                return False
    return True
    
def strCheck(b, n, m):
    if checkBoard2(b, n, m):
        return "YES"
    else:
        return "NO"

def readBoard(n, m):
    board = [0]*n
    for i in range(n):
        board[i] = map(int, raw_input().strip(' \t\n').split(" "))
    return board

def readInput():
    T = int(raw_input())
    for i in range(1, T+1):
        n, m = map(int, raw_input().split(" ", 2))
        board = readBoard(n, m)
        print "Case #%d: %s"%(i, strCheck(board, n, m))

readInput()

from random import *
def stress(n=100, m=100):
    board = [0]*n
    for i in range(n):
        board[i] = [100]*m
        mx = 100
        for j in range(0, m):
            v = randint(1, mx)
            mx = max(v, mx)
            board[i][j] = v
    print board
    print strCheck(board, n, m)

#for i in range(100):    stress(5, 5)
