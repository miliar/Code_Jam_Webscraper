#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(A):
	swaps = 0
	values = sorted(A)
	for v in values:
		pos = A.index(v)
		A1 = A[:pos]
		A2 = A[(pos+1):]
		swaps += min(len(A1), len(A2))
		A = A1 + A2
	return swaps

T = int(input())
for test in range(T):
	N = int(input())
	A = [int(i) for i in input().split()]
	print ('Case #%d:' % (test+1), solve(A))
