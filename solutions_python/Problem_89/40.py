#!/usr/bin/env python3.1

from __future__ import division

import sys
from fractions import gcd
import math

def eratosthenes(n):
	all = range(2,n+1)
	found = [1]
	while all:
		next = all[0]
		for i in range(next, n+1, next):
			if i in all:
				all.remove(i)
		found.append(next)
	return found

def cnt( primes, n): 
	c = 1
	for p in primes:
		if p == 1: continue
		x = p
		while x <= n:
			c += 1
			x *= p
	return c

prime = eratosthenes(1000)

def calc(n):
	if n == 1: return 0
	primes = [x for x in prime if x <= n][1:]
	mn = len(primes)
	mx = cnt(primes,n)
	return mx - mn


f = sys.stdin
#f = open('in')

def getints():
	return [int(x) for x in f.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	result = calc(getints()[0])
	print("Case #%d: %d" % (i+1, result))
