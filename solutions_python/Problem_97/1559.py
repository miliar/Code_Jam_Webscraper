#!/usr/bin/env python

def isCircle(a, b):
	a = str(a)
	b = str(b)
	for i in range(1, len(a)):
		j = len(a) - i
		if a[:i] == b[-i:] and a[-j:] == b[:j]:
			return True
	return False

n = int(raw_input())
for i in range(0, n):
	(a, b) = [int(j) for j in raw_input().split()]
	count = 0
	for j in range(a, b):
		for k in range(j + 1, b + 1):
			if isCircle(j, k):
				count += 1
	print "Case #%d: %d" % (i + 1, count)
