#!/usr/bin/env python2
import sys
from sets import Set

def solve(r1, a1, r2, a2):
	x1 = Set(a1[r1-1])
	x2 = Set(a2[r2-1])

	x1.intersection_update(x2)

	if len(x1) == 0:
		return "Volunteer cheated!"
	if len(x1) > 1:
		return "Bad magician!"

	return "%d" % x1.pop()

cases = int(sys.stdin.readline())

for case in range(cases):
	line = sys.stdin.readline()[:-1].split(" ")
	row1 = int(line[0])
	array1 = []
	for row in xrange(4):
		line = [ int(x) for x in sys.stdin.readline()[:-1].split(" ") ]
		array1.append(line)

	line = sys.stdin.readline()[:-1].split(" ")
	row2 = int(line[0])
	array2 = []
	for row in xrange(4):
		line = [ int(x) for x in sys.stdin.readline()[:-1].split(" ") ]
		array2.append(line)

	print "Case #%d: %s" % (case+1,solve(row1, array1, row2, array2))
		