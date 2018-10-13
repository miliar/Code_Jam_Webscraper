#! /usr/bin/python -tt

import sys
import math

def ispalindrome(a):
	a = str(a)
	return a == a[::-1]

LIMIT = 1000

palindromes = [x for x in range(1, LIMIT) if ispalindrome(x)]

squares = [x*x for x in range(1, int(math.ceil(math.sqrt(LIMIT))))]

with sys.stdin as f:
	T = int(f.readline())
	for t in range(1, T+1):
		count = 0
		(A, B) = map(int, f.readline().split())
		for n in range(A, B+1):
			if n in palindromes and n in squares and math.sqrt(n) in palindromes:
				count += 1
		print "Case #%d: %d" % (t, count)
