#!/usr/bin/python

import math

def check(k, r, t):
	return k * (2 * k + 2 * r - 1) <= t

N = int(raw_input())
for t in range(N):
	R, T = [int(x) for x in raw_input().split()]
	low, high = 1, T
	while low + 1 != high:
		mid = math.floor((low + high) / 2)
		if check(mid, R, T):
			low = mid
		else:
			high = mid
		# print low, mid, high
	print "Case #{0}: {1}".format(t + 1, int(low))