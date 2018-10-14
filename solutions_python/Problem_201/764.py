#!/bin/usr/env python

import math

def best_search(n, k):
	if k == 1:
		return (n)
	e = 0
	while 2**e <= k:
		e += 1
	e -= 1
	k -= 2**(e)
	b = 1
	l = 0
	while e > 0:
		if n % 2 == 0:
			b, l = b, b + l * 2
		else:
			b, l = b * 2 + l, l
		n /= 2
		e -= 1
	if k < b:
		return (n)
	else:
		return (n - 1)

t = int(raw_input())

for x in range(1, t + 1):
	n, k = map(int, raw_input().split(' '))
	if n == k:
		s = 1
	else:
		s = best_search(n, k)
	if s == 1:
		y, z = 0, 0
	elif s % 2 == 0:
		y, z = s / 2, s / 2 - 1
	else:
		y, z = s / 2, s / 2
	print("Case #%d: %d %d"%(x, y, z))
