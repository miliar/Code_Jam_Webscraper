#!/usr/bin/env python

def solve(x):
	friend= 0
	total = 0
	for i in range(len(x)):
		while total < i:
			friend+= 1
			total += 1
		total += x[i]
	return friend

N = int(raw_input())
for i in range(N):
	(a, b) = raw_input().split()
	x = []
	for c in b:
		x.append(int(c))
	print 'Case #' + str(i+1) + ": " + str(solve(x))
