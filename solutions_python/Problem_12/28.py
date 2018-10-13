#!/usr/bin/python

import sys

def lcs(x, y):
	if len(x) == 0 or len(y) == 0:
		return []

	best = lcs(x[:-1], y)
	best2 = lcs(x, y[:-1])
	best3 = lcs(x[:-1], y[:-1])
	best3.append(x[-1])

	if len(best2) > len(best):
		best = best2

	if x[-1] == y[-1] and (len(best3) == 1 or x[-1] != best3[-2]) and len(best3) > len(best):
		best = best3

	return best

def S(L):
	sum = 0
	ends = [1] * len(L)
	done = [0] * len(L)

	for i in range(0, len(L)):
		for j in range(0, len(ends)):
			count = ends[j]
			sum += count
			ends[j] = 0

			for k in range(j+1, len(L)):
				if L[k] > L[j]:
					ends[k] += count

		if ends == done:
			break

	return sum
		

f = open(sys.argv[1])
iters = int(f.readline())

for i in range(0, iters):
	L = f.readline().split(" ")
	n = int(L[0])
	m = int(L[1])
	X = int(L[2])
	Y = int(L[3])
	Z = int(L[4])

	A = []
	for j in range(0, m):
		A.append(int(f.readline()))

	L = []
	for j in range(0, n):
		L.append(A[j % m])
		A[j % m] = (X*A[j % m] + Y*(j + 1)) % Z

	print "Case #%d:" % (i+1), S(L) % (10**9 + 7)
