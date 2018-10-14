#!/usr/env/bin/python
from sys import argv
import re

if len(argv) < 2:
    print("Insufficient arguments. Usage: python script.py <input file> [<output file>]")
    exit()

input_file = open(argv[1])

output_file = None
if len(argv) >= 3:
    output_file = open(argv[2], 'w')

n = int(input_file.readline())


i = 1
while i <= n:
    R = int(input_file.readline())
    grid = [[]]
    alive = 0
    for r in range(R):
        (x1, y1, x2, y2) = map(int, input_file.readline()[:-1].split(" "))
        while len(grid) <= y2:
            grid.append([False for _ in grid[0]])
        while len(grid[0]) <= x2:
            for row in range(len(grid)):
                grid[row].append(False)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if not grid[y][x]:
                    grid[y][x] = True
                    alive += 1
    
    res = 0
    while alive > 0:
        for x in range(len(grid[0])-1, 0, -1):
            for y in range(len(grid)-1, 0, -1):
                if not grid[y][x] and grid[y-1][x] and grid[y][x-1]:
                    alive += 1
                    grid[y][x] = True
                elif grid[y][x] and not grid[y-1][x] and not grid[y][x-1]:
                    alive -= 1
                    grid[y][x] = False
        res += 1
    
    res = 'Case #' + str(i) + ': ' + str(res)
    print(res)
    if output_file is not None:
        output_file.write(res + '\n')
    i += 1

input_file.close()
if output_file is not None:
    output_file.close()
