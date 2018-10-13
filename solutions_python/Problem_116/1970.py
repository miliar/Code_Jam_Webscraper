#!/usr/bin/env python3

import collections
from copy import deepcopy
import functools
import itertools
import operator
import sys

def read_int():
    return int(input())

def read_ls():
    return [int(x) for x in input().split()]

def read_board():
    b = []
    for _ in range(4):
        b.append(list(input()))

    # eat blank lines between cases
    try:
        input()
    except EOFError:
        pass

    return b

def print_board(b):
    for row in b:
        for e in row:
            print(e, end="")
        print()

def check_draw(b):
    for row in b:
        for e in row:
            if e == '.':
                return False
    return True

def replace_t(b, ch):
    m = deepcopy(b)
    for r, row in enumerate(m):
        for c, e in enumerate(row):
            if e == 'T':
                m[r][c] = ch
    return m

def check_win(b):
    # check horizontal wins
    for i in range(4):
        if b[i][0] != '.' and b[i][0] == b[i][1] == b[i][2] == b[i][3]:
            return True, b[i][0], "row %d" % i

    # check vertical wins
    for i in range(4):
        if b[0][i] != '.' and b[0][i] == b[1][i] == b[2][i] == b[3][i]:
            return True, b[0][i], "col %d" % i

    # check \ win
    if b[0][0] != '.' and b[0][0] == b[1][1] == b[2][2] == b[3][3]:
        return True, b[0][0], "\\"

    # check / win
    if b[0][3] != '.' and b[0][3] == b[1][2] == b[2][1] == b[3][0]:
        return True, b[0][3], "/"

    return False, None, None

def run(b):
    assert(len(b) == 4)

    win, ch, how = check_win(replace_t(b, 'X'))
    if win:
        #print("\t", how)
        return "%s won" % ch

    win, ch, how = check_win(replace_t(b, 'O'))
    if win:
        #print("\t", how)
        return "%s won" % ch

    if check_draw(b):
        return "Draw"

    return "Game has not completed"

def verify():
    assert(True)

def main():
    for i in range(read_int()):
        # evaluate
        b = read_board()
        #print_board(b)
        result = run(b)

        # output
        print("Case #%d: %s" % (i+1, result))

if __name__ == "__main__":
    sys.exit(main())
