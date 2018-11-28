#!/usr/bin/env python2.7

from sys import stdin

def reprGrid(g):
	return '\n'.join([' '.join(map(str, row)) for row in g])

def reprGridMask(g, cells):
	g = [row[:] for row in g]
	for (i,j) in cells: g[i][j] = '*'
	return reprGrid(g)

def raiseTest(I, J, g):
	'''
	>>> g=[[2, 1, 2, 1, 2], [1, 1, 1, 1, 1], [2, 1, 2, 1, 2], [1, 1, 1, 1, 1], [2, 1, 2, 1, 2]]
	>>> raiseTest(5, 5, g)
	True
	>>> g=[[2, 2, 8, 2, 2], [2, 1, 1, 1, 2], [2, 1, 2, 1, 2], [2, 1, 1, 1, 2], [2, 2, 2, 2, 2]]
	>>> # print reprGrid(g)
	>>> raiseTest(5, 5, g)
	False
	>>> g=[[2, 2, 8, 2, 2], [2, 7, 1, 1, 2], [2, 1, 7, 1, 2], [2, 1, 1, 1, 2], [2, 2, 2, 2, 2]]
	>>> # print reprGrid(g)
	>>> raiseTest(5, 5, g)
	False
	>>> g=[[1, 1, 1, 1, 1], [2, 1, 2, 1, 2], [2, 1, 2, 1, 2], [2, 1, 2, 1, 2], [2, 1, 2, 1, 2]]
	>>> # print reprGrid(g)
	>>> raiseTest(5, 5, g)
	True
	>>> g=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	>>> raiseTest(10, 10, g)
	False
	'''
	g = [row[:] for row in g]
	zs = list( reduce(lambda zs, rowZs: zs.union(rowZs), [set(row) for row in g] ) )
	zs.sort()
	changes = -1
	currentZ = None

	for nextZ in zs:
		if currentZ == None: currentZ = nextZ; continue
		# print currentZ, '->', nextZ; print reprGrid(g); print '.'
		i_s = []
		for i in xrange(I):
			row = g[i]
			if len(set(row)) == 1: i_s.append(i)
		j_s = []
		for j in xrange(J):
			col = [row[j] for row in g]
			if len(set(col)) <= 1: j_s.append(j)

		for i in i_s:
			g[i] = [nextZ]*J
		for j in j_s:
			for row in g: row[j]=nextZ
		currentZ = nextZ

	# print reprGrid(g)

	return len( reduce(lambda zs, rowZs: zs.union(rowZs), [set(row) for row in g] ) ) == 1

def getStatus(I, J, g):
	# print reprGrid(g)
	if not raiseTest(I, J, g): return 'NO'
	return 'YES'

numcases = int(stdin.readline().strip())
for casenum in xrange(numcases):
	height, width = map(int, stdin.readline().strip().split(' '))
	lines = []
	for i in xrange(height):
		line = map(int, stdin.readline().strip().split(' '))
		lines.append(line)
	print "Case #%d: %s" % (casenum+1, getStatus(height, width, lines))
	# print lines