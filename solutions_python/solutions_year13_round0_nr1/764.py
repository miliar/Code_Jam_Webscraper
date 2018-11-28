#!/usr/bin/python

import os
import sys

fin = sys.stdin

msg_c = 'Case #%d: %s'
msg_x = 'X won'
msg_o = 'O won'
msg_d = 'Draw'
msg_g = 'Game has not completed'

def check_poss(poss, i, c):
    """Check possibility of poss[i] with c"""
    if poss[i] is not None:
        if poss[i] == '':
            poss[i] = c
        elif poss[i] != c:
            poss[i] = None

def solve(fin):
    ret = ''
    b = []
    # Populate board
    b.append(fin.readline().strip())
    b.append(fin.readline().strip())
    b.append(fin.readline().strip())
    b.append(fin.readline().strip())
    # Discard blank line after each test case
    fin.readline()
    # Possible ways to win
    poss = [''] * 10
    # Other vars
    gameNotOver = False
    for i in xrange(4):
        for j in xrange(4):
            c = b[i][j]
            if c == 'T':
                continue
            if c == '.':
                gameNotOver = True
                poss[i] = None
                poss[j + 4] = None
                if i == j:
                    poss[8] = None
                if i + j == 3:
                    poss[9] = None
                continue
            # Check for row
            check_poss(poss, i, c)
            # Check for column
            check_poss(poss, j + 4, c)
            # Check for diagonal
            if i == j:
                check_poss(poss, 8, c)
            if i + j == 3:
                check_poss(poss, 9, c)
        # Determine state of game from possibilities
    for p in poss:
        if p is not None and p != '':
            # We have a winner!
            if p == 'O':
                return msg_o
            if p == 'X':
                return msg_x
    # We did not find a winner
    if gameNotOver:
        return msg_g
    # Game is over
    return msg_d

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        print msg_c % (t, solve(fin))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
