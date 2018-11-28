#!/usr/bin/env python
import sys
#import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def wc(matrix, x, y, l):
    w = {'x':0, 'y':0}
    c = (l - 1) / 2.0
    s = 0
    for i in range(l):
        for j in range(l):
            w['x'] += (i-c) * matrix[x + i][y + j]
            w['y'] += (j-c) * matrix[x + i][y + j]
    for i in [0, l-1]:
        for j in [0, l-1]:
            w['x'] -= (i-c) * matrix[x + i][y + j]
            w['y'] -= (j-c) * matrix[x + i][y + j]
    #print x, y, i, w
    return w['x']**2 + w['y']**2 == 0

def balance(r, c, d, matrix):
    lp = min(r, c)
    for i in range(lp, 2, -1):
        for j in range(0, r - i + 1):
            for k in range(0, c - i + 1):
                if wc(matrix, j, k, i):
                    return i
    return 'IMPOSSIBLE'

case = int(lines[0])
cur = 1
for i in range(1, case + 1):
    r, c, d = [int(j) for j in lines[cur].split()]
    matrix = []
    for k in range(1, r+1):
        temp = list(lines[cur+k][:c])
        matrix.append([int(l) for l in temp])
    cur += 1 + r
    #print 'Case #%d: %s' % (i, balance(r, c, d, matrix))
    g.write('Case #%d: %s\n' % (i, balance(r, c, d, matrix)))

g.close()
