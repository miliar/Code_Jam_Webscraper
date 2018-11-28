#!/usr/bin/env python

"""
Fair Warning - python 2.6.x program by Ji Han
"""

import sys

def gcd(a, b):
	if a == 0: return b
	return gcd(b % a, a)

def diff(L):
	return list(map(long.__sub__, L[1:], L[:-1]))

def start():
	line = sys.stdin.readline()
	C = int(line)
	for i in range(1, C + 1):
		line = sys.stdin.readline()
		L = map(long, line.split())
		N, TS = L[0], sorted(L[1:])
		T = reduce(gcd, diff(TS), 0)
		print "Case #%d: %d" % (i, 0 if TS[0] % T == 0 else T - TS[0] % T)

if __name__=='__main__': 
        start()
