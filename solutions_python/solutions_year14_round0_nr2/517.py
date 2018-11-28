#!/usr/bin/env python
# -*- coding: utf-8 -*-

y = lambda C, F, X: (X*F-2*C-C*F) / (F*C)
z = lambda C, F, X, y: sum([C / (2.0+k*F) for k in xrange(int(y))])+ X/(2+y*F)

def solve(C, F, X):
	import math

	f = y(C, F, X)
	f = math.floor(f+1)
	print "%.7f" % z(C, F, X, max(0.0, f))

if __name__ == "__main__":
	T = int(raw_input())
	for i in xrange(1, T+1):
		C, F, X = map(float, raw_input().split())
		print "Case #%d:" % i,
		solve(C, F, X)