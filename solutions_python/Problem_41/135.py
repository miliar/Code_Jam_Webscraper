#!/usr/bin/env python

from copy import copy

def ans(N):
	N = list(N)
	comb = []
	for i in range(len(N)-1):
		for j in range(i+1, len(N)):
			if N[i] < N[j]:
				W = copy(N)
				W[i], W[j] = W[j], W[i]
				comb.append(int(''.join(W)))
	if comb:
		W = list(str(min(comb)))
		for i in range(len(N)-1):
			if N[i] != W[i]:
				return ''.join(W[:i+1] + sorted(W[i+1:]))
	else:
		m = N.index(min(filter(lambda x: x != '0', N)))
		N[0], N[m] = N[m], N[0]
		return N[0] + '0' + ''.join(sorted(N[1:]))


with open('in.txt') as fin:
	with open('out.txt', 'w') as fout:
		T = int(fin.readline().strip())
		for case in xrange(T):
			N = fin.readline().strip()
			print >>fout, 'Case #%d: %s' % (case+1, ans(N))
