#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def solve(X, R, C):
    R,C = min(R,C), max(R,C)
    if X > max(R,C):
        return "RICHARD"
    if X == 1:
        return "GABRIEL"
    if X == 2:
        if not (R*C)%2 == 0:
            return "RICHARD"
        return "GABRIEL"
    if X == 3:
        if not (R*C)%3 == 0:
            return "RICHARD"
        if min(R,C) <= 1:
            return "RICHARD"
        if (R,C) == (2,3):
            return "GABRIEL"
        if (R,C) == (3,3):
            return "GABRIEL"
        if (R,C) == (3,4):
            # (3,3) + 3
            return "GABRIEL"
    if X == 4:
        if not (R*C)%4 == 0:
            return "RICHARD"
        if min(R,C) <=1:
            return "RICHARD"
        if R==2:
            #  +
            # +++
            #
            return "RICHARD"
        if R==3:
            return "GABRIEL"
        if R==4:
            """
            R=3 + ++++
            """
            return "GABRIEL"

f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())
for probnum in xrange(1, problems+1):
    X, R, C = map(int, f_input.readline().rstrip().split())
    print("Case #{}: {}".format(probnum, solve(X,R,C)))
