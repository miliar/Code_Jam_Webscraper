#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

def last_upto(x, n, start="1", end="0"):
	result, i = "", 0
	while x > 0:
		result += start

		x = int(-1 + math.ceil(float(x) / float(2)))
		i += 1

	for x in xrange(n - i):
		result = result + end

	return int(result, 2)

def largest_guaranteed(n, p):
	l, r = 0, (1 << n) - 1
	while l < r:
		mid = l + (r - l + 1) / 2
		last = last_upto(mid, n)

		if last + 1 <= p:
			l = mid
		else:
			r = mid - 1

	return l

def largest_maybe(n, p):
	l, r = 0, (1 << n) - 1
	while l < r:
		mid = l + (r - l + 1) / 2
		first = last_upto((1 << n) - mid - 1, n, start="0", end="1")

		if first + 1 <= p:
			l = mid
		else:
			r = mid - 1

	return l

if __name__ == '__main__':
	T = int(sys.stdin.readline().strip())
	for CASE in xrange(1, T + 1):
		n, p = map(int, sys.stdin.readline().strip().split())

		guaranteed, maybe = largest_guaranteed(n, p), largest_maybe(n, p)
		print "Case #{}: {} {}".format(CASE, guaranteed, maybe)