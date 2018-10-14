#!/usr/bin/env python
#
#
# "Lawnmower", Qual B
# Author:   Jon Makela
# Email:    socillion@gmail.com
# Google Code Jam 2013 Qualifiers - Apr 2013

# Language: Python 2.7

import sys
from pprint import pprint

DBG = False

yes = "YES"
no = "NO"

FILE_LOC = "sample.txt"

TRAJ_OPTIONS = [[0,1],[0,-1],
                [1,0],[-1,0]]

def checkGrid(grid):
    "Returns True/False. True = Valid lawnmowable pattern"
    rows = len(grid)
    cols = len(grid[0])
    for row_idx in xrange(rows):
        for col_idx in xrange(cols):
            # got an x,y point
            if not checkPoint(grid, row_idx, col_idx):
                return False
    return True

def checkPoint(grid, y, x):
    "y aka row, x aka col. Returns True if point is mowable"
    val = grid[y][x]

    y_status = True
    x_status = True

    # search vertically
    for y_off in xrange(len(grid)):
        y_pt = grid[y_off][x]
        if y_pt > val:
            y_status = False
            break
    # search horiz
    for x_off in xrange(len(grid[0])):
        x_pt = grid[y][x_off]
        if x_pt > val:
            x_status = False
            break
    # only returns False (aka bad point) if both col and row fail check
    return (y_status or x_status)

def printResult(good):
    "good is bool, True=YES False=NO"
    if good:
        printCase(yes)
    else:
        printCase(no)

def printCase(str):
    print("Case #%d: %s" % (printCase.num,str))
    printCase.num += 1
printCase.num = 1

def readFile():
    with open(FILE_LOC) as fh:
        num_cases = int(fh.readline())
        data = []
        for i in xrange(num_cases):
            tmp = ""
            (n, m) = fh.readline().split()
            n = int(n)
            m = int(m)
            for j in xrange(n):
                tmp_ = fh.readline()
                while len(tmp_) <= 1:
                    tmp_ = fh.readline()
                tmp += tmp_
            data.append(readGrid(tmp,n,m))
    if DBG: pprint(data)
    return data

def readGrid(data, lines, cols):
    grid = []
    for line in data.splitlines():
        grid.append([int(x) for x in line.split()])
    return grid

def main():
    if len(sys.argv) > 1:
        global FILE_LOC
        FILE_LOC = sys.argv[1]
    data_grids = readFile()
    for grid in data_grids:
        is_grid_good = checkGrid(grid)
        printResult(is_grid_good)

if __name__ == '__main__':
    main()
