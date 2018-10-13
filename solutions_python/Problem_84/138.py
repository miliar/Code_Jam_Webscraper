#!/usr/bin/python

import sys

def solve(tiles, numRows, numCols):
	for i in range(0, numRows):
		for j in range(0, numCols):
			# if we find a blue tile, try to replace it
			if tiles[i][j] == '#':
				if (j+1==numCols or i+1==numRows):
					return "\nImpossible"
				if ((tiles[i][j+1]!='#') or (tiles[i+1][j]!='#') or (tiles[i+1][j+1]!='#')):
					return "\nImpossible"
				tiles[i][j] = "/"
				tiles[i][j+1] = '\\'
				tiles[i+1][j] = '\\'
				tiles[i+1][j+1] = '/'
	s = ""
	for r in tiles:
		s += "\n" + "".join(r)
	return s

f = open(sys.argv[1], 'r')
for c in range(1, int(f.readline())+1):
	# read case
	v = [int(x) for x in f.readline().split()]
	(numRows, numCols) = (v[0], v[1])
	tiles = []
	for r in range(0, numRows):
		tiles.append(list(f.readline().strip()))

	# solve and print result
	print("Case #%d:%s" % (c, solve(tiles, numRows, numCols)))
