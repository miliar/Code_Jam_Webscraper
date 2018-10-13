#!/usr/bin/python

"""
Bacteria problem solution
(GCJ 2010, Round 1B)
Author: madrezaan
"""

import sys, copy

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: bacteria.py <input file>"
    sys.exit(0)

# get number of cases
C = int(in_file.readline())

# begin prosessing cases
for cur_case in range(C):
    # get number of rectangles
    R = int(in_file.readline().strip())
    board = [[False for i in range(101)] for j in range(101)]
    min_x = [100 for i in range(101)]
    max_x = [0 for i in range(101)]
    min_y = 100
    max_y = 0
    bacterias_num = 0
    # place bacterias
    for cur_rect in range(R):
        x1, y1, x2, y2 = map(int, in_file.readline().split(" "))
        for i in range(y1, y2+1):
            if x1<min_x[i]:
                min_x[i] = x1
        if y1<min_y:
            min_y = y1
        for i in range(y1, y2+1):
            if x2>max_x[i]:
                max_x[i] = x2
        if y2>max_y:
            max_y=y2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if not board[i][j]:
                    bacterias_num += 1
                    board[i][j] = True
    # cellular automaton modelling
    steps = 0
    while bacterias_num>0:
        for j in xrange(min(100, max_y+1), min_y-1, -1):
            minx = min_x[j]-1
            maxx = min(100, max_x[j]+1)
            for i in xrange(maxx, minx, -1):
                if not board[i][j]:
                    if board[i-1][j] and board[i][j-1]:
                        board[i][j] = True
                        bacterias_num +=1
                        if i>max_x[j]:
                            max_x[j] = i
                        if j>max_y:
                            max_y = j
                else:
                    if not board[i-1][j] and not board[i][j-1]:
                        board[i][j] = False
                        bacterias_num -=1
                        if i==min_x[j]:
                            min_x[j] += 1
        steps += 1
        
    # output result
    print "Case #%d: %d" % (cur_case + 1, steps)

# close input file
in_file.close()

    
        
