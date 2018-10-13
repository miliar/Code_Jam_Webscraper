#!/usr/bin/env python

from sys import argv

if len(argv) != 2:
	print 'Usage: %s filename' % argv[0]
	exit()

inp = []

with open(argv[1]) as f:
	for line in f:
		inp.append(line[:-1])

T = int(inp.pop(0))

for i in range(len(inp)):
	inp[i] = inp[i].split(' ')
	for j in range(len(inp[i])):
		inp[i][j] = int(inp[i][j])

def test_row(row, n):
	l = len(row)

	flag1 = False
	flag2 = False

	for square in row:
		if int(square) == n:
			flag1 = True

		if int(square) > n:
			flag2 = True

	if flag1:
		if flag2:
			return False
		else:
			return True
	else:
		return True

def test_case(N, M, pattern):
	hmax = 100

	for i in range(1, hmax):
		h = hmax-i

		brow = []
		for row in pattern:
			brow.append(test_row(row, h))

		bcol = []
		for i in range(len(pattern[0])):
			col = []
			for row in pattern:
				col.append(row[i])
			bcol.append(test_row(col ,h))

		for i in range(N):
			for j in range(M):
				if pattern[i][j] == h:
					b = brow[i] or bcol[j]
					if not b:
						return 'NO'

	return 'YES'

for i in range(T):
	N = inp[0][0]
	M = inp[0][1]

	inp.pop(0)

	pattern = []

	for j in range(N):
		pattern.append(inp.pop(0))

	print "Case #%s: %s" % (i+1, test_case(N, M, pattern))








