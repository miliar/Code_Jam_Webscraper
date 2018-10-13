#! /usr/bin/env pypy
from itertools import *
T = input()
for i in xrange(1, T+1):
	S = map(int, raw_input().split())
	N, S = S[0], S[1:]
	subsets = {}
	for n in xrange(1, N):
		for s in combinations(S, n):
			v = sum(s)
			if v not in subsets:
				subsets[v] = []
			subsets[v].append(s)
	print 'Case #%d:' % i
	for v in subsets:
		if len(subsets[v]) > 1:
			print ' '.join(map(str, subsets[v][0]))
			print ' '.join(map(str, subsets[v][1]))
			break
	else:
		print 'Impossible'
