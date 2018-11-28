#!/usr/bin/env python

import os, sys

def solve( X, R, C ) :
	if X == 1 :
		return "GABRIEL"	
	
	R, C = max(R, C), min(R, C)

	if X == 2 :
		if R*C % X :
			return 'RICHARD'
		else :
			return 'GABRIEL'

	if X == 3 :
		if C < 2 :
			return 'RICHARD'
		elif R*C % X :
			return 'RICHARD'
		else :
			return 'GABRIEL'
			

	if X == 4 :
		if C <= 2 :
			return 'RICHARD'
		elif R*C % X :
			return 'RICHARD'
		else :
			return 'GABRIEL'
		
	

if __name__ == '__main__' :
	fn = sys.argv[1]
	fp = open(fn)

	T = int(fp.readline().strip())

	for i in xrange(1,T+1) :
		X, R, C = fp.readline().split()
		X, R, C = int(X), int(R), int(C)
		print "Case #%d: %s" % (i, solve(X, R, C))
