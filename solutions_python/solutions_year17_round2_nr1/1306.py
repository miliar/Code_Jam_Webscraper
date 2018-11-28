#!/usr/bin/env python

import math

test = "A-large"

f = open(test + ".in", 'r')
w = open(test + ".out", 'w')

t = int(f.readline())
for i in range(0, t):
	d, n = map(float, f.readline().split(' '))
	
	slowest = float("inf")

	for j in range(0, int(n)):
		k, s = map(float, f.readline().split(' '))

		time = (d - k) / s
		sol = float(math.floor(d / time * 1000000)) / 1000000

		if sol < slowest:
			slowest = sol

	w.write('Case #%i: %f\n' % (i + 1, slowest))

f.close()
w.close()
