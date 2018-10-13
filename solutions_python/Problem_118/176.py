#!/usr/bin/env python

f = open('list1e100', 'r')
t = [int(x) for x in f.read().split()]
f.close()

def answer(x, y):
	return bisect.bisect_right(t, y) - bisect.bisect_right(t, x-1)

import bisect

Q = int(raw_input())
for q in range(1, Q+1):
	x, y = [int(i) for i in raw_input().split()]
	print "Case #%d: %d" % (q, answer(x, y))
