#!/usr/bin/env python3
"""
Google Code Jam
2015 Round 2

Problem A. Pegman

@author yamaton
@date 2015-05-30
"""

import itertools as it
import functools
import operator
import collections
import math
import sys

DIRS = '^>v<'

def solve(xss, R, C):
    def extract_cross(i, j):
        row = [xss[i][q] for q in range(C) if q != j]
        col = [xss[p][j] for p in range(R) if p != i]
        return row + col 

    for i in range(R):
        for j in range(C):
            if xss[i][j] in DIRS and (set(extract_cross(i, j)) == {'.'} or set(extract_cross(i, j)) == set()):
                return 'IMPOSSIBLE'

    if set(it.chain.from_iterable(xss)) == {'.'}:
        return 0

    rows = [[(c, (i, j)) for j, c in enumerate(row) if c in DIRS] for i, row in enumerate(xss)]
    rows = [row for row in rows if row]
    cols = [[(c, (i, j)) for i, c in enumerate(col) if c in DIRS] for j, col in enumerate(zip(*xss))]
    cols = [col for col in cols if col]

    positions = set()
    for row in rows:
        if len(row) == 1 and row[0][0] in '<>':
            positions.add(row[0][1])
        else:
            if row[0][0] == '<':
                positions.add(row[0][1])
            if row[-1][0] == '>':
                positions.add(row[-1][1])

    for col in cols:
        if len(col) == 1 and col[0][0] in 'v^':
            positions.add(col[0][1])
        else:
            if col[0][0] == '^':
                positions.add(col[0][1])
            if col[-1][0] == 'v':
                positions.add(col[-1][1])

    # print_stderr(positions)
    return len(positions)


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input())+1):
        print("Case #%d: " % _tc, end='')
        R, C = [int(s) for s in input().strip().split()]
        xss = [input().strip() for _ in range(R)]
        assert len(xss[0]) == C

        # print_stderr('\n--------- case #%d -------' % _tc)
        # for xs in xss:
        #     print_stderr(xs)        
        # print_stderr('')

        result = solve(xss, R, C)
        print(result)

        print_stderr('result =', result)


if __name__ == '__main__':
    main()
