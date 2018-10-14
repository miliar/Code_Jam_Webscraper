#!/usr/bin/env python
# encoding: utf-8

import sys

C = int(sys.stdin.readline())

for t in xrange(0, C):
    R = int(sys.stdin.readline())
    min_x, min_y, max_x, max_y = 1000000, 1000000, 0, 0
    rect = []
    for r in xrange(0, R):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        rect.append((x1, y1, x2, y2))
        
        if x1 < min_x:
            min_x = x1    
        if x2 > max_x:
            max_x = x2          
        if y1 < min_y:
            min_y = y1           
        if y2 > max_y:
            max_y = y2
            
    dx = max_x - min_x + 1
    dy = max_y - min_y + 1
    
    M = [[0] * dx for i in xrange(0, dy)]
    nb = 0
    for x1, y1, x2, y2 in rect:
        for y in xrange(y1, y2+1):
            for x in xrange(x1, x2+1):   
                if not M[y-min_y][x-min_x]:
                    nb += 1   
                    M[y-min_y][x-min_x] = 1
                    
    c = 0
    while nb:
        c += 1
        for y in xrange(dy-1, -1, -1):
            for x in xrange(dx-1, -1, -1):
                if M[y][x] == 1:
                    if x == 0 and y == 0:
                        M[y][x] = 0
                        nb -= 1
                    elif x == 0 and M[y-1][x] == 0:
                        M[y][x] = 0
                        nb -= 1 
                    elif y == 0 and M[y][x-1] == 0:
                        M[y][x] = 0
                        nb -= 1
                    elif M[y-1][x] == 0 and M[y][x-1] == 0:
                        M[y][x] = 0
                        nb -= 1
                else:          
                    if x > 0 and y > 0 and M[y-1][x] == 1 and M[y][x-1] == 1:
                        M[y][x] = 1
                        nb += 1
        
    print "Case #%d: %d" % (t+1, c) 