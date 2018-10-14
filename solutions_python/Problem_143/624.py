#/usr/bin/python

import sys

t = int(sys.stdin.readline())

for ii in range(t):
	n = map(int,sys.stdin.readline().split())

	count = 0
	for i in range(n[0]):
		for j in range(n[1]):
			if (i&j < n[2]):
				count += 1

	print "Case #{0:0d}:".format(ii+1), count