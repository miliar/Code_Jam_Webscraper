# coding: utf-8

import os, sys, re, string
import math,random

def next_int():
	return int(sys.stdin.readline())
def next_ints():
	return map(int, sys.stdin.readline().split())

def calc_cost(N, n):
	v = n - 1
	return (2*N - v) * (v + 1) / 2

def total_cost(N, v):
	res = 0
	for o, e, p in v:
		res += calc_cost(N, e - o) * p
	return res

def solve(N, M, v):
	total = total_cost(N, v)
	m = [0] * (N + 3)
	for o, e, p in v:
		for i in xrange(o, e):
			m[i] += p
	minv = 0
	while True:
		minpos, maxpos = N + 3, 0
		checkvalue = -1
		for i in xrange(N + 3):
			if m[i] > 0:
				minpos = i
				checkvalue = m[i]
				break
		if minpos == N + 3:
			break
		for i in xrange(minpos + 1, N + 3):
			if m[i] == 0:
				maxpos = i
				break
			else:
				checkvalue = min(checkvalue, m[i])
		minv += calc_cost(N, maxpos - minpos) * checkvalue
		for i in xrange(minpos, maxpos):
			m[i] -= checkvalue
	return total - minv

def main():
	for i in xrange(next_int()):
		N, M = next_ints()
		p = [next_ints() for j in xrange(M)]
		result = solve(N, M, p)
		print "Case #%d: %d" % (i + 1, result)

if __name__ == '__main__':
	main()


