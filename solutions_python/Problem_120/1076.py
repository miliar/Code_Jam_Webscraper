#!/usr/bin/env python

import sys, math

T = int(sys.stdin.readline())

def max_rings(r, t):
	a1 = math.pow(r+1, 2) - math.pow(r, 2)
	a2 = math.pow(r+3, 2) - math.pow(r+2, 2)
	d = a2 - a1
	circles_painted = 0
	paint_used = 0
	while paint_used <= t:
		circles_painted += 1
		paint_used += a1 + (circles_painted - 1) * d
	return circles_painted - 1

def solve():
	line = sys.stdin.readline().strip()
	if line == '':
		line = sys.stdin.readline().strip()
	r, t = line.split(' ')
	res = max_rings(int(r), float(t))
	return res

for t in range(T):
	result = solve()
	print "Case #%d: %s" % (t+1, result)
