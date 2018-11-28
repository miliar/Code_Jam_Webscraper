#!/usr/bin/env python
# input stdin, output stdout
"""
Input example:

4
2 2 2
2 1 3
4 4 1
3 2 3
"""
import sys


def solve(i):
    X, R, C = map(int, sys.stdin.readline().split())
    num_spots = R * C

    if X == 1:
        outcome = 'GABRIEL'

    elif num_spots % X == 0:
        if R == 1 or C == 1:
            if X == 2:
                outcome = 'GABRIEL'
            else:
                outcome = 'RICHARD'
        else:
            if X == 4 and (R == 2 or C == 2):
                outcome = 'RICHARD'
            else:
                outcome = 'GABRIEL'
    else:
        outcome = 'RICHARD'

    print "Case #%d: %s" % (i, outcome)


def main():
    num_testcases = int(sys.stdin.readline().strip())
    for t in range(num_testcases):
        solve(t + 1)

if __name__ == '__main__':
    main()
