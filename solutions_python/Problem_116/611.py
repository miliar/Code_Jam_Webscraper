#!/bin/python
import re
t = int(raw_input().strip())
counter = 0
for game in range(t):
    grid = []
    for row in range(4):
        grid.append(raw_input().strip())
    if counter != t - 1:
        blankline = raw_input() # newline
        counter += 1

    allpatterns = []
    patterns = [[(0,0),(1,1),(2,2),(3,3)],
                [(0,3),(1,2),(2,1),(3,0)],
                [(0,0),(0,1),(0,2),(0,3)],
                [(1,0),(1,1),(1,2),(1,3)],
                [(2,0),(2,1),(2,2),(2,3)],
                [(3,0),(3,1),(3,2),(3,3)],
                [(0,0),(1,0),(2,0),(3,0)],
                [(0,1),(1,1),(2,1),(3,1)],
                [(0,2),(1,2),(2,2),(3,2)],
                [(0,3),(1,3),(2,3),(3,3)]]
    for pattern in patterns:
        p = ""
        for coord in pattern:
            p += grid[coord[0]][coord[1]]
        allpatterns.append(p)

    
    unfinished = False
    for row in grid:
        if re.match("\.", row):
            unfinished = True
    decided = False
    for p in allpatterns:
        if not decided:
            if re.match('^[XT]+$', p):
                print "Case #{0}: X won".format(game+1)
                decided = True
            elif re.match('^[OT]+$', p):
                print "Case #{0}: O won".format(game+1)
                decided = True
    if not decided:
        if unfinished:
            print "Case #{0}: Game has not completed".format(game+1)
        else:
            print "Case #{0}: Draw".format(game+1)

