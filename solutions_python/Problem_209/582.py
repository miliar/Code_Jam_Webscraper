#!/usr/bin/env python2
import math
import sys

sys.setrecursionlimit(10000)

memo = [[0 for x in range(1)] for y in range(1)]

def border(R,H):
	return 2 * math.pi * R * H

def top(R):
	return math.pi * (R**2)

def solve(K, P, p=0, n=0, first=True):
	if n==K or p==len(P):
			return 0

	if memo[p][n] > -1.:
		return memo[p][n]

	r1 = 0
	if first:
		r1 += top(P[p][0])
	r1 += border(P[p][0],P[p][1]) + solve(K,P,p+1, n+1, False)
	r2 = solve(K,P,p+1, n, first)

	# print p, P[p], r1, r2
	memo[p][n] = max(r1,r2)
	return memo[p][n]

cases = int(sys.stdin.readline())

for case in range(cases):
	N,K = map(int, sys.stdin.readline()[:-1].split(' '))
	memo = [[-1. for x in range(N)] for y in range(N)]
	P = []
	for r in xrange(N):
		P.append([ int(x) for x in sys.stdin.readline()[:-1].split(' ')])
	P.sort()
	P.reverse()
	# print N,K
	print ("Case #%d: %.9f" % (case+1,solve(K,P)))
	# print solve(K,P)
