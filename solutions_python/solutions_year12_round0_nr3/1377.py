#!/usr/bin/python
# coding: utf-8

import sys, itertools

def cantRep(n, b):
	s = str(n)
	l = len(s)
	res = set()
	for i in range(l):
		m = s[i:] + s[:i]
		if m[0] != '0' and int(m) > n and int(m) <= b:
			res.add(int(m))
			# print n, m, b
	return len(res)

if __name__ == "__main__":
	# Solve
	tt = int(raw_input().rstrip('\n'))
	for i in range(tt):
		a, b = map(int, raw_input().split())
		r = 0
		for n in range(a, b):
			r += cantRep(n, b)
		print 'Case #%d: %d' % (i+1, r)
