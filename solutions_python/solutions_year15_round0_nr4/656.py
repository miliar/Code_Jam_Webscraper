#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    X, R, C = [int(x) for x in cipher.split()]
    # print X, R, C
    if X == 1:
        return True
    elif X > R * C:
        return False
    elif R * C % X != 0:
        return False
    elif R * C == X and X > 2:
        return False
    elif (R * C) % 2 == 0 and X == 2:
        return True
    elif X - R == 1 or X - C == 1:
        return True
    elif X > R or X > C:
        return False
    return True

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        winner = ('GABRIEL' if solve(cipher) else 'RICHARD')
        print("Case #%i: %s" % (caseNr, winner))
