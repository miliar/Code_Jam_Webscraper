#!/usr/bin/python
import sys

def inc(a, x):
	for i in range(x):
		a += (a-1)
	return a

def solvable(a, n):
	ctr = 0
	for i in range(0, len(n)):
		found = False
		diff = len(n)-i
		for c in range(diff):
			tmp = inc(a, c)
			if tmp > n[i]:
				a = tmp + n[i]
				ctr += c
				found = True
				break
		if not found:
			ctr += 1

	return ctr


t = int(sys.stdin.readline())
for ctr in range(1, t+1):
	a, _ = [int(x) for x in sys.stdin.readline().split()]
	n = [int(x) for x in sys.stdin.readline().split()]
	n.sort()

	print "Case #{0}: {1}".format(ctr, int(solvable(a, n)))