#!/usr/bin/python2

import sys, os, string, re

arr = []

def permute(ix, P, best):
	if ix == n:
		cost = 0
		prison = P*[1]
		m = len(prison)
		for i in range(n):
			mid = arr[i]-1
			prison[mid] = 0
			pos = mid-1
			while (pos >= 0) and (prison[pos] == 1):
				cost += 1
				pos -= 1
			pos = mid+1
			while (pos < m) and (prison[pos] == 1):
				cost += 1
				pos += 1
		best = min(best, cost)
		return best
	best = permute(ix+1, P, best)
	t = arr[ix]
	for i in range(ix+1, n):
		arr[ix] = arr[i]
		arr[i] = t
		best = permute(ix+1, P, best)
		arr[i] = arr[ix]
	arr[ix] = t
	return best

in_file = sys.stdin
N = int(in_file.readline())
for case_num in range(N):
	[P, Q] = map(int, in_file.readline().strip().split())
	arr = map(int, in_file.readline().strip().split())
	n = len(arr)
	best = permute(0, P, n*P)

	print 'Case #%d: %d' % (case_num+1, best)
