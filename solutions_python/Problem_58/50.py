#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline())

def iswin(a,b):
	m = min(a, b)
	n = max(a, b)
	if m == n:
		return False
	if n/m >= 2:
		return True
	if n%m == 0:
		return True
	if n/m == 1:
		return not iswin(n-m, m)

for case in range(1, T+1):
	A1, A2, B1, B2 = [int(s) for s in sys.stdin.readline().split()]
	res = 0
	for i in range(A1, A2+1):
		for j in range(B1, B2+1):
			if iswin(i, j) == True:
				res = res + 1
	
	print "Case #%d: %d"%(case, res)

