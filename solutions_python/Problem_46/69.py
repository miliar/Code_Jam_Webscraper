#!/usr/bin/python

import sys

def isok(row, r):
    return row[r+1:] == '0'*(len(row)-r-1)

def bubble(rows, r, x):
    if r == len(rows) - 1:
	return x
    if isok(rows[r], r):
	return bubble(rows, r+1, x)
    for s in range(r+1, len(rows)):
	if isok(rows[s], r):
	    break
    return bubble(rows[0:r] + rows[s:s+1] + rows[r:s] + rows[s+1:], r+1, x + (s-r))

f = open(sys.argv[1])
T = int(f.readline().strip())
for t in range(1, T+1):
    N = int(f.readline().strip())
    matrix = []
    for n in range(N):
	matrix.append(f.readline().strip())
    x = bubble(matrix, 0, 0)
    print 'Case #%d: %d' % (t, x)
