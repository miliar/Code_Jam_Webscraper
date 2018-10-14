#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys
import fractions

lines = sys.stdin.readlines()

T = int(lines[0])

def solve(R, k, N, g):
	mappings = {}
	mappings[1] = {}
	for n in range(N):
		need = 0
		earned = 0
		moved = 0
		for groups in range(N):
			gidx = (n + groups) % N
			if (need + g[gidx] <= k):
				need += g[gidx]
				earned += g[gidx]
				moved += 1
			else: break
		mappings[1][n] = (earned, moved)
	mult = 1
	while mult <= R:
		mappings[mult * 2] = {}
		for n in range(N):
			(e1, m1) = mappings[mult][n]
			(e2, m2) = mappings[mult][(n + m1) % N]
			mappings[mult * 2][n] = (e1 + e2, (m1 + m2) % N)
		mult *= 2
	total_earned = 0
	rounds_remaining = R
	idx = 0
	mult = 1
	while rounds_remaining > 0:
		if rounds_remaining % 2:
			(e, m) = mappings[mult][idx]
			total_earned += e
			idx = (idx + m) % N
		rounds_remaining //= 2
		mult *= 2
	return total_earned

for t in range(1, T + 1):
	RkN = lines[t*2-1].split()
	R = int(RkN[0])
	k = int(RkN[1])
	N = int(RkN[2])
	g = [int(x) for x in lines[t*2].split()]
	assert(N == len(g))
	#~ print R, k, N, g
	answer = solve(R, k, N, g)
	print "Case #%d: %s" % (t, answer)
