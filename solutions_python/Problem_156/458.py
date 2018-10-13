#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def solve(x):
	x.sort(reverse=True)
	m = x[0]
	res = x[0]
	for r in range(1, m+1):
		s = 0
		for z in x:
			if z <= r:
				break
			s += int(math.ceil(z / float(r))) - 1
		if s + r < res:
			res = s + r
	return res

for i in range(int(raw_input())):
	a = raw_input()
	b = raw_input().split()
	x = []
	for n in b:
		x.append(int(n))
	print 'Case #' + str(i+1) + ": " + str(solve(x))
