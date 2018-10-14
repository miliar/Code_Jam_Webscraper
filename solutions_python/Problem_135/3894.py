#!/usr/bin/python

import sys

def getRow(r):
	for l in xrange(4):
		if l==r :
			row = f.readline().split()
		else :
			f.readline()
	return row

if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	cases = int(f.readline())

	for t in xrange(cases):
		row1 = getRow(int(f.readline())-1)
		row2 = getRow(int(f.readline())-1)

		luckyNum = set(row1).intersection(row2)


		if len(luckyNum) == 1:
			print "Case #{0}: {1}".format(t, ''.join(luckyNum))
		elif len(luckyNum) > 1:
			print "Case #{0}: Bad magician!".format(t)
		elif len(luckyNum) == 0:
			print "Case #{0}: Volunteer cheated!".format(t)