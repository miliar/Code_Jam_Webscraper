#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
	print 'Need Input!'
	sys.exit()

f=open(sys.argv[1],'r')
numcases = int(f.readline())
for i in range(1, numcases+1):
	print "Case #" + str(i) + ": ",
	line = f.readline()
	line = line.split()
	n = int(line[0])
	A = int(line[1])
	B = int(line[2])
	C = int(line[3])
	D = int(line[4])
	X = int(line[5])
	Y = int(line[6])
	M = int(line[7])
	trees = []
	trees.append((X,Y))
	for j in range(1, n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		trees.append((X,Y))
	trisfound = 0
	for j in range(0, n-2):
		for k in range(j+1, n-1):
			for l in range(k+1, n):
				xr = (trees[j][0] + trees[k][0] + trees[l][0]) % 3
				yr = (trees[j][1] + trees[k][1] + trees[l][1]) % 3
				if xr == 0 and yr == 0:
					trisfound += 1
	print trisfound
