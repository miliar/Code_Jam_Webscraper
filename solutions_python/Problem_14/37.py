#!/usr/bin/env python
import sys
import math
import string

num_cases = -1

fileIN = open(sys.argv[1], "r")

num_cases = int(fileIN.readline())

n = -1
m = -1
a = -1


def dub_tri_area(a, b, c):
    return abs(b[0]*a[1] - a[0]*b[1] + c[0]*b[1] - b[0]*c[1] + a[0]*c[1] - c[0]*a[1])
    
    
def calcpoints(n, m, a):
    if a == 0:
        return "0 0 0 0 0 0"
    
    if a > (n * m):
        return "IMPOSSIBLE"
    
    if a == (n * m):
        return "0 0 %i %i %i %i" % (n, m, n, 0)
    
    point1 = (0, 0)
    
    for i in range(0, n+1):
        for j in range(0, m+1):
            for k in range(0, n+1):
                for l in range(0, m+1):
                    if dub_tri_area((0,0),(i,j),(k,l)) == a:
                        return "%d %d %d %d %d %d" % (i, j, k, l, 0, 0)
            #if dub_tri_area(point1, (i,j), (0,j)) == a:
            #    return "%d %d %d %d %d %d" % (point1[0], point1[1], i, j, 0, j)
            #if dub_tri_area(point1, (i,j), (i,0)) == a:
            #    return "%d %d %d %d %d %d" % (point1[0], point1[1], i, j, i, 0)
            #if dub_tri_area(point1, (i,j), (0,j)) == a:
            #   return "%d %d %d %d %d %d" % (point1[0], point1[1], i, j, 0, j)
            #if dub_tri_area((i,j), (n,m), (n,0)) == a:
            #    return "%d %d %d %d %d %d" % (i, j, n, m, n, 0)
    return "IMPOSSIBLE"
        
    
    
    

for case_num in range(num_cases):
    items = fileIN.readline().split()
    n = int(items[0])
    m = int(items[1])
    a = int(items[2])
    
    outstring = str(calcpoints(n, m, a))
    sys.stdout.write("Case #" + str(case_num+1) + ": " + outstring + "\n")