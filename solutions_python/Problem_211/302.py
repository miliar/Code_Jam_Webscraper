#!/usr/bin/env python


def calc(u, p, n, k):
	p.sort()
	for i in xrange(0, n):
		if u == 0:
			break
		if u > i * (p[i] - p[0]):
			add = p[i] - p[0]
			u = u - i * (p[i] - p[0])
		else:
			add = u / i
			u = 0
		for k in xrange(0, i):
			p[k] += add

	add = u / n
	for i in range(0, n):
		p[i] += add

	result = 1
	for i in range(0, n):
		result *= p[i]
	if result > 1:
		return 1.0
	else:
		return result

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	u = float(raw_input())
	p = [float(s) for s in raw_input().split(" ")]
	print "Case #{}: {}".format(i, calc(u, p, n, k))