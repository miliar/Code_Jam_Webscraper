#!/usr/bin/env python

import sys

f = sys.stdin

T = int(f.readline().strip())

def den_is_power_2(p,q):
	x = q
	assert x >= 1
	while x > 1:
		if x%2 != 0:
			if x == p: return True
			return False
		x = x / 2.
	return True

def simplify(p,q):
	while p%2 == 0 and q%2 == 0:
		p, q = p/2., q/2.
	return p, q

for i in range(1, T+1):
	p, q = [float(x) for x in f.readline().strip().split('/')]
	p, q = simplify(p,q)
	if not den_is_power_2(p,q):
		print "Case #%s: impossible" % i
		continue
	gen = 1
	x = p/q*2**gen - 1
	out_break = 0
	while x < 0:
		if gen > 40:
			print "Case #%s: impossible" % i
			out_break = 1
			break
		gen += 1
		x = p/q*2**gen - 1
	if out_break == 1: continue
	print "Case #%s: %s" % (i, gen)
