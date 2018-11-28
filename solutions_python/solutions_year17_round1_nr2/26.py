#!/usr/local/bin/python3

from fractions import Fraction

getl = lambda: input().strip().split()
get = lambda: tuple(map(int, getl()))

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap


def solve(N, P, R, Q):
	sentinel = -1e10

	events = [e for i, (qs, r) in enumerate(zip(Q, R)) for q in qs for e in ((Fraction(q) / r * 10 / 11, False, i), (Fraction(q) / r * 10 / 9, True, i))] + \
	         [(i, True, sentinel) for i in range(1, 1100100)]

	active = [0] * N
	inactive = [0] * N

	kits = 0

	for position, end, i in sorted(events):
		if i is sentinel:
			while all(active):
				kits += 1
				for j in range(N):
					active[j] -= 1
					inactive[j] += 1
		else:
			if not end:
				active[i] += 1
			else:
				if inactive[i]:
					inactive[i] -= 1
				else:
					active[i] -= 1

	return kits


testCases, = get()
for testCase in range(1, testCases + 1):
	N, P = get()
	R = get()
	Q = tuple(tuple(sorted(get())) for i in range(N))
	print('Case #{}: {}'.format(testCase, solve(N, P, R, Q)))

