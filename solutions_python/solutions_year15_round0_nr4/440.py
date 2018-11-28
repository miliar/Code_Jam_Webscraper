#!/usr/bin/env python3
# coding=utf-8

"""
  Solution to Qualification Round.C

  Author: killerrex@gmail.com
"""

import sys


lim_row = [
    0,  # 0-Mino -> Always solvable
    0,  # 1-Mino -> Always solvable
    0,  # 2-Mino -> Solvable if the space is even
    1,  # 3-Mino -> If row is 1 the tile in L cannot be fit
    2,  # 4-Mino -> For row 1 or 2 the tile in T cannot be fit
    3,  # 5-Mino -> The piece in W cannot fit for 1, 2 or 3 rows
    3,  # 6-Mino -> The piece in ~W cannot be fit
]


def omino(x, r, c):
    """
    Solve the case
    :param x: N-Omino size
    :param r: Rows
    :param c: Cols
    :return: True if it is solvable
    """

    # Get R <= C
    if r > c:
        r, c = c, r

    # Check the area first...
    if r*c % x != 0:
        return False

    # For X=>7 we can always use a tile with a hole in the middle
    if x > len(lim_row):
        return False

    # The row limit is the maximum row that guarantee that there is a
    # tile that cannot be solved, no matter the number of cols
    return r > lim_row[x]


def solve(fd):

    cases = int(fd.readline().strip())

    for k in range(cases):
        x, r, c = [int(c) for c in fd.readline().strip().split()]

        if omino(x, r, c):
            winner = 'GABRIEL'
        else:
            winner = 'RICHARD'
        print("Case #{}: {}".format(k+1, winner))


if __name__ == '__main__':

    # Read stdin and write stdout
    solve(sys.stdin)
