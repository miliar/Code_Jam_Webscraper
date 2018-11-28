#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(o, e, n):
	d = e - o
	return d * n - d * (d - 1) / 2

def unique(s):
	ret = []
	for i in range(len(s)):
		if i != 0 and s[i - 1] == s[i]:
			pass
		else:
			ret.append(s[i])
	return ret

def main():
	T = getLineAs(int)[0]

	for cc in range(T):
		(n, m) = getLineAs(int)

		original = 0
		cnto = {}
		cnte = {}

		for i in xrange(m):
			(o, e, p) = getLineAs(int)
			original += p * calc(o, e, n)

			if not o in cnto: cnto[o] = 0
			if not o in cnte: cnte[o] = 0
			if not e in cnto: cnto[e] = 0
			if not e in cnte: cnte[e] = 0
			cnto[o] += p
			cnte[e] += p

		stations = sorted(sorted(cnto) + sorted(cnte))
		stations = unique(stations)
		cand = []

		ans = 0
		for s in stations:
			if s in cnto:
				cand.append( (s, cnto[s]) )

			if s in cnte:
				p = cnte[s]

				while p > 0:
					if cand[-1][1] > p:
						ans += p * calc(cand[-1][0], s, n)
						cand[-1] = (cand[-1][0], cand[-1][1] - p)
						p = 0
					elif cand[-1][1] == p:
						ans += p * calc(cand[-1][0], s, n)
						p = 0
						cand.pop()
					else:
						ans += cand[-1][1] * calc(cand[-1][0], s, n)
						p -= cand[-1][1]
						cand.pop()

		print "Case #%d: %d" % (cc + 1, original - ans)

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
