#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""See http://martin-thoma.com for more mini code samples."""


def solve(X, R, C):
    """
    Parameters
    ----------
    X : int, 1<=X<=20
        Onimoto formed by X unit squares joined along their edges
    R : int, 1<=X<=20
        Width of the board
    C : int, 1<=X<=20
        Heights

    Returns
    -------
    str
        RICHARD if the one choosing the Onimoto wins,
        GABRIEL if the one filling the grid wins
    """
    if X == 1:
        return "GABRIEL"
    if X >= 7 or R*C % X != 0 or R*C < X:
        # The empty chell in the middle is a killer-strategy
        # ... the other two are fails in game design
        return "RICHARD"

    if X > max(R, C):
        return "RICHARD"

    import math
    if 1+int(math.floor((X-1)/2)) > min(R, C):
        return "RICHARD"

    # From now on:
    # * R >= 2
    # * C >= 2
    # * R*C >= X
    # * R*C % X == 0

    if X <= 3:
        return "GABRIEL"
    if X == 4:
        if R == 2 or C == 2:
            return "RICHARD"
        else:
            return "GABRIEL"
    return "dunno"


if __name__ == "__main__":
    testcases = int(raw_input())

    for caseNr in range(1, testcases+1):
        X, R, C = [int(el) for el in raw_input().split(" ")]
        print("Case #%i: %s" % (caseNr, solve(X, R, C)))
