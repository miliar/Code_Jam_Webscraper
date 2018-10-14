#!/usr/local/bin/python

# A. Square Tiles

import math
import sys
from fractions import gcd

f = sys.stdin
T = int(f.readline())

for x in range(1, T+1):
	list = [int(e) for e in f.readline().split()]
	R = int(list[0])
	C = int(list[1])

	tile = []
	for r in range(R):
		tile.append([c for c in f.readline().strip()])

	for i in range(R-1):
		for j in range(C-1):
			if tile[i][j] == '#':
				if tile[i][j+1] == '#' and tile[i+1][j] == '#' and tile[i+1][j+1] == '#':
					tile[i][j] = '/'
					tile[i][j+1] = '\\' 
					tile[i+1][j] = '\\'
					tile[i+1][j+1] = '/'

	containBlue = False
	for line in tile:
		for c in line:
			if c == '#':
				containBlue = True
				break

	print "Case #%d:" % x
	if containBlue:
		print 'Impossible'
	else:
		for line in tile:
			print ''.join(line)
