#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	T = getLineAs(int)[0]

	for c in range(T):
		(k, n) = getLineAs(int)

		keys = getLineAs(int)
		need = array(n)
		have = array(n)
		cnts = array(201)

		for key in keys:
			cnts[key] += 1

		for i in range(n):
			line = getLineAs(int)
			need[i] = line[0]
			have[i] = line[2:]

		memo  = array(1 << n, False)
		route = []

		def solve(f):
			if f == 0:
				raise Exception

			if memo[f]:
				return

			memo[f] = True

			for i in range(n):
				if (f & (1 << i)) and cnts[need[i]] > 0:
					cnts[need[i]] -= 1
					for h in have[i]:
						cnts[h] += 1
					route.append(i + 1)

					solve(f ^ (1 << i))

					for h in have[i]:
						cnts[h] -= 1
					cnts[need[i]] += 1
					route.pop()

		print "Case #%d:" % (c + 1),
		try:
			solve((1 << n) - 1)
			print "IMPOSSIBLE"
		except Exception:
			print " ".join(map(str, route))

	return 0

## -------------------------------------------
## TEMPLATE

from sys import stdin
from sys import setrecursionlimit
from copy import deepcopy

def getline():
	return stdin.readline()

def getLineAs(tp):
	return map(tp, getline().split())

def array(n, init = 0):
	return [deepcopy(init) for i in range(n)]

if __name__ == "__main__":
	setrecursionlimit(1024 * 1024)
	main()
