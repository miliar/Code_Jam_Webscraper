#!/usr/bin/python

# Run by:
#     cat input | a.py

import sys
from math import sqrt

l = sys.stdin.readline()
n = int(l)

for i in range(n):
    print 'Case #%d:' % (i+1,),

    l = sys.stdin.readline()
    (n, A, B, C, D, x0, y0, M) = [int(x) for x in l.split()]

    trees = []
    X = x0
    Y = y0
    trees.append((X, Y))
    for j in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X, Y))
    
    triangles = 0
    for j in range(n):
        for k in range(j+1, n):
            for m in range(k+1, n):
                (X,Y) = ((trees[j][0] + trees[k][0] + trees[m][0]) / 3.0, (trees[j][1] + trees[k][1] + trees[m][1]) / 3.0)
                if abs(X - int(X)) < 0.00001 and abs(Y - int(Y)) < 0.00001:
                    triangles += 1

    print triangles
    
