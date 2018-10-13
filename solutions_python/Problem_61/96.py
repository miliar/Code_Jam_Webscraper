#!/usr/bin/env python3

import itertools

def build_s(n, i=0):
	if i < n-1:
		for e in build_s(n, i+1):
			yield [i+2] + e
			yield e
	else:
		yield []
		return

def check_s(s, n):
	if not s:
		return False
	s.sort()
	if s[-1] != n:
		return False
	c = n
	while c != 1:
		try:
			c = s.index(c) + 1
		except ValueError:
			return False
	return True

cache = {}

t = int(input())
for x in range(t):
	n = int(input())
	if n in cache:
		y = cache[n]
	else:
		y = 0
		for s in build_s(n):
			if check_s(s, n):
				y += 1
		cache[n] = y
	print('Case #%d: %d' % (x + 1, y % 100003))
