#!/usr/bin/python

fp = open('p2.in')

def canCreate(grid):
    maxRows = [max(x) for x in grid]
    maxCols = []
    
    for i in range(len(grid[0])):
        maxCols.append(max([x[i] for x in grid]))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < maxRows[i] and grid[i][j] < maxCols[j]:
                return False                
    
    return True

cases = int(fp.readline())
cc = 1

while cases > 0:
    m, n = [int(x) for x in fp.readline()[:-1].split(' ')]
    c = 0
    grid = []
    
    while c < m:
        grid.append([int(x) for x in fp.readline()[:-1].split(' ')])
        c = c + 1
    
    works = canCreate(grid)
    
#    print grid
    
    if (works):
        print "Case #%d: YES" % cc
    else:
        print "Case #%d: NO" % cc
        
    
    cc = cc + 1
    cases = cases - 1
