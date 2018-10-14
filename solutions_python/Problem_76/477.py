#!/usr/bin/env python

import sys

lines = [x.strip() for x in sys.stdin.readlines()]

lines = lines[2::2]

results = []

def getComb(x, size, c=[]) :
    if size == 1 :
        rc = reduce(xor, c, 0)
        rx = reduce(xor, x, 0)
        for i in x :
            if xor(i, rc) == xor(i, rx) :
                return sum(x) - i
        return -1
    else :
        for i in x : 
            y = [a for a in x if a != i]
            m = getComb(y, size-1, c + [i])
            if m >= 0 :
                return m
        return -1
                
def xor(x, y) :
    return x ^ y
 
cnt = 0
for l in lines :
    cnt += 1
    points = sorted([int(x) for x in l.split()])

    if reduce(xor, points, 0) != 0 :
        results.append('NO')
        continue

    r = -1
    for i in range(1, len(points)/2 + 1) :
        r = getComb(points, i)
        if r >= 0 :
            break 
        
    results.append(r)
                
for i in range(len(results)): 
    print "Case #" + str(i+1) + ": " + str(results[i])
