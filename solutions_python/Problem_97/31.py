#!/usr/bin/env python
import cj

# def string_rotations(x):
# 	s = str(x)
# 	for i in xrange(1, len(s)):
# 		yield int(s[-i:] + s[:-i])

def rotations(x):
	L = len(str(x))
	p, q = 10, 10 ** (L - 1)
	while True:
		y = x % p * q + x / p
		if x != y:
			yield y
			p *= 10
			q /= 10
		else:
			break

def find(A, B):
	count = 0
	for n in xrange(A, B + 1):
		for m in rotations(n):
			if n < m and m <= B:
				yield n, m

pairs = [pair for pair in find(1, 2000000)]

def solve(A, B):
	count = 0
	for n, m in pairs:
		if  A <= n and m <= B:
			count += 1
		if n > B:
			break
	return count

cj.jam(lambda reader: (reader/int, reader/int), solve)