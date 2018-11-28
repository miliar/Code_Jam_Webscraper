#! /usr/bin/python

from sys import stdin

def fetch_row(file):
	row_nb = int(file.readline())
	for i in xrange(4):
		if i == (row_nb-1):
			row = [int(x) for x in file.readline().split()]
		else:
			file.readline()

	return row


if __name__ == '__main__':
	
	N = int(stdin.readline())

	for i in xrange(N):
		row1 = fetch_row(stdin)
		row2 = fetch_row(stdin)
		intersect = [x for x in row1 if x in row2]

		if len(intersect) == 1:
			print "Case #%d:" % (i+1), intersect[0]
		elif len(intersect) == 0:
			print "Case #%d: Volunteer cheated!" % (i+1)
		else:
			print "Case #%d: Bad magician!" % (i+1)
