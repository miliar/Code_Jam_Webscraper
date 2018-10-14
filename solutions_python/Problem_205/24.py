#!/usr/local/bin/python3
from sys import setrecursionlimit as slr
slr(10**5)

from fractions import Fraction

getl = lambda: input().strip().split()
get = lambda: tuple(map(int, getl()))

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap


def solve(Hd, Ad, Hk, Ak, B, D):

	HD = Hd

	seen = dict()

	def dfs(Hd, Ad, Hk, Ak):
		if Hk <= 0:
			return 0
		if Hd <= 0:
			return None
		if Ak < 0:
			Ak = 0

		state = (Hd, Ad, Hk, Ak)
		if state in seen:
			return seen[state]
		seen[state] = None

		#print(state)

		if Ad >= Hk:
			seen[state] = 1

		else:
			outcomes = [
				dfs(Hd - max(Ak - D, 0), Ad, Hk, Ak - D),
				dfs(Hd - Ak, Ad, Hk - Ad, Ak),
				dfs(HD - Ak, Ad, Hk, Ak),
				dfs(Hd - Ak, Ad + B, Hk, Ak),
			]
			if any(o is not None for o in outcomes):
				seen[state] = 1 + min(o for o in outcomes if o is not None)

		return seen[state]

	return dfs(Hd, Ad, Hk, Ak)


testCases, = get()
for testCase in range(1, testCases + 1):
	
	Hd, Ad, Hk, Ak, B, D = get()
	result = solve(Hd, Ad, Hk, Ak, B, D)
	if result is None: result = 'IMPOSSIBLE'
	print('Case #{}: {}'.format(testCase, result))

