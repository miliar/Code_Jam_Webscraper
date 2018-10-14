#!/usr/bin/env python
import cj

def read(reader):
	N = reader/int
	s = [reader/int for _ in xrange(N)]
	return N, s

def solve(N, s):
	X = sum(s)
	l = 0.0
	r = 1.0 * X
	while r - l > 1e-8:
		m = (l + r) / 2
		t = 0.0
		for j in s:
			if j < m:
				t += m - j
		if t > X:
			r = m
		else:
			l = m
	y = []
	for j in s:
		if j > m:
			y.append(0)
		else:
			y.append(1.0 * (m - j) / X)
	return ' '.join([str(100 * item) for item in y])

cj.jam(read, solve)