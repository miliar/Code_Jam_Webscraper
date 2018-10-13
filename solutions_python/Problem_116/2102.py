#!/usr/bin/env python

import sys

Board = 16 * "."

Pos = ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15),
       (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15),
       (0, 5, 10, 15), (3, 6, 9, 12))

def Win(player):
    for t in Pos:
        won = True
        for p in t:
            won = won and ((Board[p] == player) or (Board[p] == "T"))
        if won:
            #print "%s won:" % (player,), t
            return True
    return False

def Solve(no):
    global Board

    b = ""
    b += sys.stdin.readline()[:-1]
    b += sys.stdin.readline()[:-1]
    b += sys.stdin.readline()[:-1]
    b += sys.stdin.readline()[:-1]
    sys.stdin.readline()
    Board = b

    if Win("X"): status = "X won"
    elif Win("O"): status = "O won"
    elif "." in Board: status = "Game has not completed"
    else: status = "Draw"
    print "Case #%d: %s" % (no, status)

T = int(sys.stdin.readline())
for no in range(1, T+1):
    Solve(no)

