#!/usr/bin/python

import sys
import math

def same(arr):
    flag = 'T'
    for i in range(0,4):
        if arr[i] =='.':
            return False
        elif arr[i] == 'X':
            if flag == 'O':
                return False
            else:
                flag = 'X'
        elif arr[i] == 'O':
            if flag == 'X':
                return False
            else:
                flag = 'O'
    return True

def full(board):
    for line in board:
        for grid in line:
            if grid == '.':
                return False
    return True

def test(board):
    for i in range(0,4):
        if same([board[i][j] for j in range(0,4)]): return board[i][0]
        if same([board[j][i] for j in range(0,4)]): return board[0][i]
    
    if same([board[j][j] for j in range(0,4)]): return board[0][0]
    if same([board[j][3-j] for j in range(0,4)]): return board[0][3]

    if full(board):
        return 'D'
    else:
        return 'C'

if __name__=="__main__":
    fp = sys.stdin
    data = fp.readlines()
    N = int(data[0])
    boards = [[line.strip() for line in data[i*5+1:i*5+5]] for i in xrange(0,N)]
    for i,board in enumerate(boards):
        res = test(board)
        print "Case #%d:" %(i+1),
        if res == 'X' or res == 'O':
            print res,"won"
        elif res == 'D':
            print "Draw"
        else:
            print "Game has not completed"


