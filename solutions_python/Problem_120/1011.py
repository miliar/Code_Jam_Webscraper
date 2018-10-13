#!/usr/bin/python3

import sys
import math

def bullseye(r, t):
	i = 0
	paint = 0
	while paint < t:
		rb = r + 2 * i + 1
		rw = r + 2 * i
		paint += rb * rb - rw * rw
		if paint <= t:
			i += 1
	return i


T = int(sys.stdin.readline().strip())
for i in range(0, T):
	l = sys.stdin.readline().strip()
	l = l.split(' ')
	r = int(l[0])
	t = int(l[1])
	ans = bullseye(r, t);
	print("Case #{}: {}".format(i+1, ans))
