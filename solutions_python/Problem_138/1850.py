#!/usr/bin/env python3

from itertools import product, combinations


def read_ints():
	return map(int, input().strip().split())

def read_floats():
	return map(float, input().strip().split())

def response(x, s):
	x = list(filter(lambda y: y>x, s))

	if len(x)==0:
		return min(s)

	else:
		return min(x)

def deceitful(a, b):
	b = set(b)
	a = sorted(a)

	result = 0

	for x in a:
		resp = response(x, b)

		# find the best cheat
		for y in a:
			r = response(y, b)

			if (r<x and r<y) or (r>x and r>y) and r>resp:
				resp = r

		b.remove(resp)

		if resp<x:
			result += 1


	return result

def war(a, b):
	a = sorted(a)
	b = set(b)

	result = 0

	for x in a:
		resp = response(x, b)
		b.remove(resp)

		if resp<x:
			result += 1

	return result
	

def testcase():
	n, = read_ints()
	a = list(read_floats())
	b = list(read_floats())

	return '{} {}'.format(deceitful(a,b), war(a,b))


T, = read_ints()
for t in range(T):
	print('Case #{}: {}'.format(t+1, testcase()))
