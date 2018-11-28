#!/usr/bin/env python2
import sys
import math

def ringsurface(out_r):

	in_r = out_r - 1
	out_a = out_r * out_r
	in_a = in_r * in_r 
	
	return out_a - in_a


def solve(r,t):

	remain = t
	cr = r+1
	res = 0

	while remain > 0:
		remain -= ringsurface(cr)
		if remain < 0:
			break
		res += 1
		cr += 2

	return res

cases = int(sys.stdin.readline())

for case in range(cases):
	line = sys.stdin.readline()[:-1].split(" ")
	r = int(line[0])
	t = int(line[1])
	print "Case #%d: %s" % (case+1,solve(r,t))
