#!/usr/bin/env python3

from itertools import *

def read_ints():
	return map(int, input().strip().split())


def diff(a, b):
	for num, p in enumerate(zip(a, b)):
		x, y = p
		if x != y:
			return num
	return min(len(a), len(b))

def nodesnum(s):
	if not s:
		return 0
	num = 1
	s.sort()
	if s:
		num += len(s[0])

	for a, b in zip(s[:-1], s[1:]):
		num += len(b)-diff(a,b)		

	return num
		

def test():
	m, n = read_ints()
	strings = [input() for _ in range(m)]
	results = []

	for opt in product(*[list(range(n)) for _ in range(m)]):
		sets = [[] for _ in range(n)]
		for (o, s) in  zip(opt, strings):
			sets[o].append(s)

		num = sum([nodesnum(s) for s in sets])
		results.append(num)

	max_res = max(results)
	count = sum(map(lambda x: x == max_res, results))

	return '{} {}'.format(max_res, count)

def x():
	T, = read_ints()
	for x in range(T):
		print("Case #{}: {}".format(x+1, test()))

if __name__ == "__main__":
	x()
