cases = input()
from itertools import *
for i in range(cases):
    rows,cols = map(int,raw_input().split())
    grid = []
    for j in range(rows):
        grid.append(list(raw_input()))
    #copy initials forward across rows
    for row,col in product(range(rows),range(1,cols)):
        if grid[row][col]=="?":
            grid[row][col]=grid[row][col-1]
    #copy initials backward across rows
    for row,col in product(range(rows),range(cols-2,-1,-1)):
        if grid[row][col]=="?":
            grid[row][col]=grid[row][col+1]
    #all that's left is empty rows
    for row in range(1,rows):
        if grid[row][0]=="?":
            grid[row]=grid[row-1]
    #and the same thing backwards to the beginning
    for row in range(rows-2,-1,-1):
        if grid[row][0]=="?":
            grid[row]=grid[row+1]
    print "Case #%d:"%(i+1)
    for row in grid:
        print "".join(row)