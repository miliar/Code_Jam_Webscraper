#!/usr/local/bin/python
import sys
import heapq
import math


def solve(count):
    R, C = sys.stdin.readline().split()
    R = int(R)
    C = int(C)
   
    grid = [0] * R
    isEmpty = [True] * R
    for r in range(R):
        grid[r] = list(sys.stdin.readline().strip())

        lastC = None
        for c in range(C):
            if grid[r][c] == '?':
                if (lastC != None):
                    grid[r][c] = lastC
            else:
                if (lastC == None):
                    for i in range(c):
                        grid[r][i] = grid[r][c]
                lastC = grid[r][c]
                isEmpty[r] = False

    lastRow = None
    for r in range(R):
        if isEmpty[r]:
            if lastRow != None:
                grid[r] = lastRow
        else:
            if lastRow == None:
                for i in range(r):
                    grid[i] = grid[r]
            lastRow = grid[r]

    print "Case #{}:".format(case+1)
    for row in grid:
        print ''.join(row)

cases = int(sys.stdin.readline())
for case in range(cases):
    solve(case + 1)
