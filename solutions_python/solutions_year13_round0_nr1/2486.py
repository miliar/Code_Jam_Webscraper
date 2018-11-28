#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *


sample = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O"""


"XXXT .... OO.. .... X.O. X.O. X... T... X... .O.T"


def find_winner(row):
    T = row.count("T")
    if T + row.count("X") == 4:
        return "X"
    elif T + row.count("O") == 4:
        return "O"
    return None

def solve(input):
    T = int(input.pop(0))
    for X in xrange(1, T+1):
        rows = [input.pop(0).strip() for _ in xrange(4)]
        rows += ["".join(row[n] for row in rows) for n in xrange(4)]
        rows += ["".join(rows[n][n] for n in xrange(4))]
        rows += ["".join(rows[3-n][n] for n in xrange(4))]

        full = True
        winner = None
        for row in rows:
            winner = find_winner(row)
            if winner is not None:
                break
            if full and row.find(".") > -1:
                full = False

        Y = "%s won" % (winner,) if winner is not None else "Draw" if full else "Game has not completed"
        print "Case #%d: %s" % (X, Y)

        if X < T:
            input.pop(0)

        #print rows


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            solve(f.readlines())
    else:
        solve(sample.split("\n"))


