#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys
import math

lines = sys.stdin.readlines()

T = int(lines[0])

def get_cost(Minv, things, depth, startpt):
	if sum(Minv) == 0:
		return 0
	if depth < 0: return 1000000000
	cost_of_match = things[depth][startpt]
	if len(Minv) == 1:
		return cost_of_match
	Minv_smaller = [max(0, x - 1) for x in Minv]
	mididx = len(Minv) // 2
	with_match = cost_of_match + get_cost(Minv_smaller[:mididx], things, depth-1, startpt*2) + get_cost(Minv_smaller[mididx:], things, depth-1, startpt*2+1)
	without_match = get_cost(Minv[:mididx], things, depth-1, startpt*2) + get_cost(Minv[mididx:], things, depth-1, startpt*2+1)
	return min(with_match, without_match)

idx = 1
for t in range(1, T + 1):
	P = int(lines[idx])
	M = lines[idx + 1].split()
	Minv = [P - int(x) for x in M]
	#print "P =", P, "Minv =", Minv
	things = []
	for p in range(P):
		moo = [int(x) for x in lines[idx + 2 + p].split()]
		things.append(moo)
	idx += P + 2
	answer = get_cost(Minv, things, P-1, 0)
	print "Case #%d: %s" % (t, answer)
