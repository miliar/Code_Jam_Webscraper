#!/usr/bin/python

import sys

def getrow():
	rowchosen = int(sys.stdin.readline())
	for r in range(1, 5):
		row = sys.stdin.readline()
		if r == rowchosen:
			rowchosen = row
	return set(rowchosen.split())

n = int(sys.stdin.readline())
for c in range(1, n + 1):
	sys.stdout.write("Case #" + str(c) + ": ")

	set1 = getrow()
	set2 = getrow()
	common = set1.intersection(set2)

	if len(common) == 0:
		print "Volunteer cheated!"
	elif len(common) > 1:
		print "Bad magician!"
	else:
		print str(common.pop())
