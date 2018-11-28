#!/usr/bin/env python
import cj

def read(reader):
	A, B = reader/int, reader/int
	p = [reader/float for _ in xrange(A)]
	return A, B, p

cache = {}

def find(A, B, p):
	if A == 0:
		return B + 1
	if not ( A in cache ):
		c1 = 1 + B + 1

		x = 1.0
		for i in xrange(A):
			x *= p[i]
		c2 = x * (B - A + 1) + (1 - x) * (B - A + 1 + B + 1)

		m = min(c1, c2)

		for k in xrange(1, A + 1):
			c3 = k + find(A - k, B, p) 
			if (c3 < m):
				m = c3;

		cache[A] = m
		return m
	else:
		return cache[A]


def solve(A, B, p):
	global cache 
	cache = {}
	return find(A, B, p)

cj.jam(read, solve)