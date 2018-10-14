#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def intersect(i, j):
	if i == j:
		return 0
	if (i[0]-j[0])*(i[1]-j[1]) < 0:
		return 1
	else:
		return 0

T = int(sys.stdin.readline())

for cc in range(1, T+1):
	N = int(sys.stdin.readline())
	ps = []
	for i in range(0, N):
		a, b = [int(s) for s in sys.stdin.readline().split()]
		pr = (a,b)
		ps.append(pr)
	
	num = 0
	l = len(ps)
	for i in range(0, l):
		for j in range(i+1, l):
			num = num + intersect(ps[i], ps[j])
	
	print "Case #%d: %d"%(cc, num)

