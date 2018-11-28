#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput as f
from collections import Counter
X = "X won"
O = "O won"
DRAW = "Draw"
IC = "Game has not completed"

def check_board(b):
    """docstring for check_board"""
    complete = True

    def check_four(four):
        c = Counter(four)
    
        def helper():
            for p in ['X','O']:
                if c[p] == 4 or (c[p] == 3 and c['T'] == 1):
                   return p
        if helper() == 'X':
            return X
        if helper() == 'O':
            return O
        return None

    def check_columns():
        for c in range(len(b)):
            col = '' 
            for r in range(len(b)):
                col += b[r][c]
            x = check_four(col)
            if x:
                return x

    def check_rows():
        for r in b:
            if '.' in r:
                complete = False
            w = check_four(r)
            if w:
                return w
        return None

    def check_diagonals():

        diag = '' 
        rev = ''
        for i in range(4):
            diag += b[i][i]
        for i in range(len(b)):
            rev += b[3-i][i]
        d = check_four(diag)
        r = check_four(rev)
        if d is not None:
            return d
        if r is not None:
            return r
        return None

    def complete():
        for r in b:
            if '.' in r:
                return False
        return True

    winner = [x for x in [check_rows(),check_columns(),check_diagonals()] if x is not None]
    if winner:
        return winner[0]
    if complete(): 
        return DRAW
    else:
        return IC

def get_boards():
    """gets board data from input file"""
    boards = []
    board = []
    for line in f.input():
        if f.lineno() == 1:
            T = line.rstrip('\n')
            continue
        if line == "\n":
            boards.append(board)
            board = []
        else:
            l = line.split()
            for c in l:
                board.append(c)
    return boards

def main():
    """docstring for main"""
    for i, board in enumerate(get_boards()):
        print "Case #%d: %s" % (i + 1, check_board(board))

if __name__ == '__main__':
    main()
