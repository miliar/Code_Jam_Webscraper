#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print "oops"
	sys.exit(1)

f = open(sys.argv[1], "r")

numCases = int(f.readline())

for i in range(numCases):
	coord = []
	tmp = f.readline().split()
	n = int(tmp[0])
	A = int(tmp[1])
	B = int(tmp[2])
	C = int(tmp[3])
	D = int(tmp[4])
	x = int(tmp[5])
	y = int(tmp[6])
	M = int(tmp[7])
	
	coord.append((x, y))

	for j in range(n):
		x = ((A * x) + B) % M
		y = ((C * y) + D) % M
		coord.append((x, y))

	r = 0

	for x in range(n):
		for y in range(x + 1, n):
			for z in range(y + 1, n):
				if (coord[x][0] + coord[y][0] + coord[z][0]) % 3 == 0:
					if (coord[x][1] + coord[y][1] + coord[z][1]) % 3 == 0:
						r += 1
	print "Case #" + str(i + 1) + ": " + str(r)
