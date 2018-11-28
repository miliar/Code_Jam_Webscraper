
"""
AABC
??BC

AB?
???

AAB
?C?

AC?
?C?

A??
???
??B

AC?
?C?
??B

A??
???
C?B

A
?
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*args):
    print(*args, file=sys.stderr)

def intersects(r1, r2):
    if (r1[1] > r2[3]) or (r1[3] < r2[1]):
        return False
    if (r1[0] > r2[2]) or (r1[2] < r2[0]):
        return False
    return True

global grid, r, c, placements, R, C
fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    R, C = map(int, fin.readline().split())
    grid = []
    chars = set()
    placements = []
    for i in range(R):
        grid.append(fin.readline().strip())
        placements.append(list(grid[-1]))
        for c in grid[-1]:
            if c != '?':
                chars.add(c)

    chars = sorted(list(chars))
    debug(chars)
    N = len(chars)

    corners = {}
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '?':
                continue

            char = grid[r][c]
            if char in corners:
                existing = corners[char]
                corners[char] = (min(existing[0], r), min(existing[1], c), max(existing[2], r), max(existing[3], c))
            else:
                corners[char] = (r, c, r, c)


    def can_place(r, c, char):
        existing = corners[char]
        ccorners = (min(existing[0], r), min(existing[1], c), max(existing[2], r), max(existing[3], c))
        for oc, ocorners in corners.items():
            if oc == char:
                continue
            if intersects(ccorners, ocorners):
                return False

        return True


    def place(r, c, char):
        existing = corners[char]
        ccorners = (min(existing[0], r), min(existing[1], c), max(existing[2], r), max(existing[3], c))
        corners[char] = ccorners

    def get_char(r, c):
        for oc, ocorners in corners.items():
            if intersects(ocorners, (r, c, r, c)):
                return oc
        return '!'



    for r in range(R):
        for c in range(C):
            if grid[r][c] != '?':
                continue
            placed = False
            for char in chars:
                if can_place(r, c, char):
                    place(r, c, char)
                    placed = True
                    break
            if not placed:
                raise "Could not place!"

    result = ''
    for r in range(R):
        for c in range(C):
            result += get_char(r, c)
        if r != R - 1:
            result += '\n'

    # debug(result)


    print("Case #%d:\n%s" % (case, result))

