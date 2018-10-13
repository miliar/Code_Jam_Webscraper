#!/usr/bin/env python3

import sys

def isRecycled(n, m):
	ns, ms = str(n), str(m)
	if len(ns) != len(ms): return False
	for shift in range(1, len(ns)):
		if ms == ns[-shift:] + ns[:-shift]: return True
	return False

def solve(a, b):
	c = 0
	for n in range(a, b):
		for m in range(n+1, b+1):
			if isRecycled(n,m): c += 1
	return c

numcases = int(sys.stdin.readline())
for i in range(numcases):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	print("Case #%d: %d" % (i+1, solve(a, b)))
