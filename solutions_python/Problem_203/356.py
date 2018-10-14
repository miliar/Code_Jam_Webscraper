
import os
import sys
import glob
import subprocess
import random
import fileinput


next_line = 0
lines = [line.strip() for line in fileinput.input()]
def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]


def calc():
    R, C = [int(i) for i in get_line().split()]
    grid = []
    for i in range(R):
        grid.append([c for c in get_line()])

    for i in range(R):
        for j in range(C):
            if grid[i][j] != '?':
                k = j - 1
                while k >= 0:
                    if grid[i][k] != '?':
                        break
                    grid[i][k] = grid[i][j]
                    k = k - 1
                k = j + 1
                while k < C:
                    if grid[i][k] != '?':
                        break
                    grid[i][k] = grid[i][j]
                    k = k + 1

    for i in range(R):
        for j in range(C):
            if grid[i][j] != '?':
                k = i - 1
                while k >= 0:
                    if grid[k][j] != '?':
                        break
                    grid[k][j] = grid[i][j]
                    k = k - 1
                k = i + 1
                while k < R:
                    if grid[k][j] != '?':
                        break
                    grid[k][j] = grid[i][j]
                    k = k + 1

    return grid

T = int(get_line())
for i in range(1, T + 1):
    grid = calc()
    print('Case #%d:' % i)
    for g in grid:
        print(''.join(g))
