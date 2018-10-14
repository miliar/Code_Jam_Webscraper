#!/usr/bin/python

import sys
import math

if __name__ == '__main__':
	filename = sys.argv[1]

	try:
		infile = open(filename)
	except:
		print "Couldn't open file: %s" % filename
		sys.exit(1)

	numcases = int(infile.readline())

	for case in range(1, numcases + 1):

		n, m = infile.readline().strip().split(" ")
		n = int(n)
		m = int(m)

		lawn = []
		possible = 'YES'
		max_vert = []
		max_horiz = []

		for i in range(n):
			lawn.append(infile.readline().strip().split(" "))
			max_horiz.append(max(lawn[i]))
		
		for i in range(m):
			max_vert.append(max(lawn[x][i] for x in range(n)))

		if not ((n == 1) or (m == 1)):

			for i in range(n):
				for j in range(m):
					value = lawn[i][j]
					if (value < max_horiz[i]) and (value < max_vert[j]):
						possible = 'NO'
						break

		print "Case #%s: %s" % (case, possible)
