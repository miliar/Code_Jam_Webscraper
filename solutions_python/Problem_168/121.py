#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys

EMPTY = (-1, -1)

def debug(*args):
    print(*args, file=sys.stderr)


def count(grid, rows, cols):

    cc = 0

    for i, (m, n) in enumerate(rows):
        if m == -1:
            continue
        elif m == n:
            e = grid[i][m]
            if e == '<' or e == '>':
                if cols[m][0] == cols[m][1]:
                    raise "IMPOSSIBLE"
                else:
                    cc += 1
            else:
                # Will handle in column pass
                pass
        else:
            if grid[i][m] == '<':
                cc += 1
            if grid[i][n] == '>':
                cc += 1

    for j, (m, n) in enumerate(cols):
        if m == -1:
            continue
        elif m == n:
            e = grid[m][j]
            if e == '^' or e == 'v':
                if rows[m][0] == rows[m][1]:
                    raise Exception("IMPOSSIBLE")
                else:
                    cc += 1
            else:
                # Will handle in column pass
                pass
        else:
            if grid[m][j] == '^':
                cc += 1
            if grid[n][j] == 'v':
                cc += 1

    return cc

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    R,C = map(int, fin.readline().split())
    rows = [EMPTY]*R
    cols = [EMPTY]*C
    grid = []
    for i in range(R):
        row = fin.readline().strip()
        grid.append(row)
        for j, c in enumerate(row):
            if c != '.':
                if rows[i] == EMPTY:
                    rows[i] = (j, j)
                else:
                    rows[i] = (min(rows[i][0], j), max(rows[i][1], j))

                if cols[j] == EMPTY:
                    cols[j] = (i, i)
                else:
                    cols[j] = (min(cols[j][0], i), max(cols[j][1], i))


    debug(rows)
    debug(cols)
    debug('--')

    try:
        cc = count(grid, rows, cols)
    except:
        cc = 'IMPOSSIBLE'


    print("Case #%d: %s" % (case, cc))

