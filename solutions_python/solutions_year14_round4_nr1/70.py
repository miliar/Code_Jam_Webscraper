#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(X, S):
	complete_discs = 0
	discs = []
	S.sort()
	S.reverse()
	for size in S:
		discs.sort()
		stored = False
		for i, d in enumerate(discs):
			if d + size <= X:
				discs.pop(i)
				complete_discs += 1
				stored = True
				break
		if not stored:
			discs.append(size)
	return complete_discs + len(discs)

T=int(input())
for test in range(T):
	[N,X] = [int(i) for i in input().split()]
	S = [int(i) for i in input().split()]
	print ('Case #%d:' % (test+1), solve(X, S))
