#!/usr/bin/python

import sys
from math import sqrt, floor

DBG = False

def log(s):
	if DBG:
		print s

def p(s):
	sys.stdout.write(s)

def is_palindrom(a):
	s = str(a)
	l = len(s)
	if l == 1:
		return True
	m = l / 2
	i = 0
	while i < m:
		if s[i] != s[l-i-1]:
			return False
		i += 1
	return True

def solve(A, B):
	curr = int(floor(sqrt(A)))
	log("curr=" + str(curr))
	sq = curr*curr
	n = 0
	while sq <= B:
		if is_palindrom(curr) and is_palindrom(sq) and sq >= A:
			n += 1
		curr += 1
		sq = curr*curr
	return str(n)

n = int(raw_input())

for j in xrange(1, n+1):
	A, B = [int(_) for _ in raw_input().strip().split()]
	
	p("Case #" + str(j) + ": ")

	p(solve(A, B))

	p("\n")