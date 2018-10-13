#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem D. Ominous Omino
# https://code.google.com/codejam/contest/6224486/dashboard#s=p3
#

import sys


def solve(X, R, C):
    if C < R:
        # always R < C
        R, C = C, R

    if (R * C) % X > 0:
        # never cannot fill stage
        return 'RICHARD'
    if X == 1 or X == 2:
        # always can fill stage
        return 'GABRIEL'
    elif X == 3:
        if R == 1:
            # Richard choose:
            # X
            # XX
            return 'RICHARD'
        # at least 2x3 stage, can fill any 2 possible 3-ominoes
        # ABB  AAA
        # AAB  BBB
        return 'GABRIEL'
    elif X == 4:
        if R <= 2:
            # Richard choose:
            # XX
            # .XX
            return 'RICHARD'
        # at least 3x4 stage, can fill use any 5 possible 4-ominoes
        # AABB  ABBB  AABB
        # AABB  AABC  CAAB
        # CCCC  ACCC  CCCB
        return 'GABRIEL'
    elif X == 5:
        if R <= 3:
            # Richard choose:
            # X
            # XX
            # .XX
            return 'RICHARD'
        # at least 4x5 stage, can fill use any 12 possible 5-ominoes
        return 'GABRIEL'
    elif X == 6:
        if R <= 3:
            return 'RICHARD'
        # at least 4x6 stage, can fill use any 6-ominoes
        return 'GABRIEL'
    else:  # X >= 7
        # Richard can choice 'in hall' omino
        # example:
        # xx
        # x.x
        # xxx
        return 'RICHARD'


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        X, R, C = map(int, IN.readline().strip().split())
        OUT.write('Case #%d: %s\n' % (index + 1, solve(X, R, C)))


def makesample():
    print 64
    for X in range(1, 5):
        for R in range(1, 5):
            for C in range(1, 5):
                print X, R, C


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

