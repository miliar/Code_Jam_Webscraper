#!/usr/bin/env python

import sys

def rotate(data, N):
    for i in range(N):
	data[i] = data[i].replace('.', "").rjust(N, '.')

def find(data, N, K, c, starta, startb, da, db):
    a, b = starta, startb
    l = 0
    while a >= 0 and b >= 0 and a < N and b < N:
	if data[a][b] == c:
	    l += 1
	    if l == K:
		return True
	else:
	    l = 0
	a += da
	b += db
    return False

def check(data, N, K, c):
    for i in range(N):
	if find(data, N, K, c, i, 0, 0, 1):
	    return True
	if find(data, N, K, c, 0, i, 1, 0):
	    return True
	if find(data, N, K, c, i, 0, 1, 1):
	    return True
	if find(data, N, K, c, 0, i, 1, 1):
	    return True
	if find(data, N, K, c, i, 0, -1, 1):
	    return True
	if find(data, N, K, c, N - 1, i, -1, 1):
	    return True
    return False

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    N, K = map(long, inputfile.readline().strip().split())
    data=[]
    for n in range(N):
	data.append(inputfile.readline().strip())

    rotate(data, N)
    red = check(data, N, K, 'R')
    blue = check(data, N, K, 'B')
    if red:
	if blue:
	    y = 'Both'
	else:
	    y = 'Red'
    else:
	if blue:
	    y = 'Blue'
	else:
	    y = 'Neither'

    print "Case #%d: %s" % (case, y)
