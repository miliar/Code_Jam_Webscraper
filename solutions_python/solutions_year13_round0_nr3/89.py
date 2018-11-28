#!/usr/bin/python

import sys
from bisect import bisect_left

def ispalin(s):
	for i in xrange(len(s) / 2):
		if s[i] != s[len(s) - i - 1]:
			return False
	return True

def palindromes(limit):
	def genpalin(s, n, limit):
		if n <= limit and (s % 10 == 0 or ispalin(str(s**2))):
			if s % 10 != 0:
				yield s
			for d in xrange(10):
				for p in genpalin(10**(n + 1) * d + 10 * s + d, n + 2, limit):
					yield p
	
	for p in genpalin(0, 0, limit):
		yield p

	for i in xrange(0, 10):
		for p in genpalin(i, 1, limit):
			yield p

def sqpalin(limit):
	for p in palindromes(limit):
		yield p**2

sqpalins = sorted([p for p in sqpalin(50)])

T = int(raw_input().strip())

for nCase in xrange(1, T+1):
	A,B = map(int, raw_input().strip().split())
	print "Case #%d: %d" % (nCase, bisect_left(sqpalins, B+1) - bisect_left(sqpalins, A))
