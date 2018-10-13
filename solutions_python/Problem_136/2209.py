#/usr/bin/python

import sys

t = int(sys.stdin.readline())

for ii in range(t):
	m = map(float, sys.stdin.readline().split())

	result = 0.0
	grow = 2.0

	while ((m[0]/grow + m[2]/(grow+m[1])) < (m[2]/grow)):
		result += m[0]/grow
		grow += m[1]
	result += m[2]/grow

	print "Case #{0:0d}:".format(ii+1),result