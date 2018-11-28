#!/usr/bin/env python
import sys

def checkwin(board, symbol):
    for r in range(0, 4):
        win = True
        for c in range(0, 4):
            if board[r][c] not in ['T', symbol]:
                win = False
                break
        if win:
            return True
    for c in range(0, 4):
        win = True
        for r in range(0, 4):
            if board[r][c] not in ['T', symbol]:
                win = False
                break
        if win:
            return True
    win = True
    for c in range(0, 4):
        if board[c][c] not in ['T', symbol]:
            win = False
            break
    if win:
        return True
    win = True
    for c in range(0, 4):
        if board[3-c][c] not in ['T', symbol]:
            win = False
            break
    if win:
        return True

    return False

def checkdraw(board):
    for r in range(0, 4):
        for c in range(0, 4):
            if board[r][c] == '.':
                return False

    return True

def solve():
    B = []
    for i in range(4):
        B.append(sys.stdin.readline())
    sys.stdin.readline()

    if checkwin(B, 'X'):
        return 'X won'

    if checkwin(B, 'O'):
        return 'O won'

    if checkdraw(B):
        return 'Draw'

    return 'Game has not completed'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        print 'Case #%d: %s' % (t, solve())
