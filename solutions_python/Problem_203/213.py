#!/usr/bin/env python
from math import *
from sys import *

numcases = int(stdin.readline())

for case in range(1,numcases+1):
    print "Case #" + str(case) + ":"
    size = map(int,stdin.readline().split())
    R = size[0]
    C = size[1]
    grid = []
    for i in range(R):
        chars = list(stdin.readline())
        chars = chars[:(len(chars)-1)]
        grid.append(chars)
    for i in range(R):
        for j in range(1,C):
            if grid[i][j-1] !="?" and grid[i][j] == "?":
                grid[i][j] = grid[i][j-1]
        for j in range(C-2,-1,-1):
            if grid[i][j+1] !="?" and grid[i][j] == "?":
                grid[i][j] = grid[i][j+1]
    for i in range(1,R):
        if "?" in grid[i]:
            grid[i] = grid[i-1]
    for i in range(R-1,-1,-1):
        if "?" in grid[i]:
            grid[i] = grid[i+1]
    for i in range(R):
       for j in range(C):
           stdout.write(grid[i][j])
       print


    











