#!/usr/bin/python

import sys
import os

nCases = int(sys.stdin.readline().strip(" \r\n"))

for case in xrange(1, nCases+1):
	[n, m] = map(int, sys.stdin.readline().strip(" \r\n").split(" "))
	
	rows = [map(int, sys.stdin.readline().strip(" \r\n").split(" ")) for _ in xrange(n)]
	
	columns = [map(lambda e : e[i], rows) for i in xrange(m)]
	
	#print str(rows)
	#print str(columns)
	
	# The lowest height you can cut in a given direction is equal to the maximum height in that row
	min_rows = map(lambda e : max(e), rows)
	min_cols = map(lambda e : max(e), columns)

	#print str(min_rows)
	#print str(min_cols)

	possible = True
	for y in xrange(n):
		for x in xrange(m):
			
			if rows[y][x] < min_rows[y] and rows[y][x] < min_cols[x]:
				# Can't have gone through a row or column to cut this square	
			#	print "%d,%d (%d vs %d vs %d) BAD" % (x, y, rows[y][x], max_rows[y], max_cols[x])
				possible = False
				break
			#print "%d,%d (%d vs %d vs %d) ok" % (x, y, rows[y][x], max_rows[y], max_cols[x])
		if not possible:
			break		
	if possible:
		print "Case #%d: YES" % case
	else:
		print "Case #%d: NO" % case
	