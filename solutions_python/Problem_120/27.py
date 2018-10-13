#! /usr/bin/env python
# -*- coding: utf-8 -*-

def solve(r, t):
	low   = 0
	high  = 2 ** 64
	start = r * 2 + 1

	while low <= high:
		mid = (low + high) / 2
		use = mid * (start + 2 * (mid - 1))
		if t < use:
			high = mid - 1
		else:
			low  = mid + 1

	if t < 1000:
		assert high == solveMin(r, t)

	return high

def solveMin(r, t):
	ret = 0
	while True:
		use = (r + 1) ** 2 - r ** 2
		if t - use < 0:
			break
		t   -= use
		ret += 1
		r   += 2

	return ret

def main():
	T = input()

	for cc in xrange(1, T + 1):
		(r, t) = map(int, raw_input().split())
		print "Case #%d: %d" % (cc, solve(r, t))

	return 0

## -------------------------------------------
## TEMPLATE

from sys import stdin
from sys import setrecursionlimit
from copy import deepcopy
from math import sqrt
from itertools import permutations
from itertools import combinations

def getline():
	return stdin.readline()

def getLineAs(tp):
	return map(tp, getline().split())

def array(n, init = 0):
	return [deepcopy(init) for i in range(n)]

def count_if(lst, pred):
	ret = 0
	for i in lst:
		if pred(i): ret = ret + 1
	return ret

def toSepStr(lst):
	if len(lst):
		return "".join([str(item) + " " for item in lst])[:-1]
	else:
		return ""

if __name__ == "__main__":
	setrecursionlimit(1024 * 1024)
	main()
