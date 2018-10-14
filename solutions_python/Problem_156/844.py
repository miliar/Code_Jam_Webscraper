#!/usr/bin/env python
import heapq
import math
from copy import copy

from collections import Counter


def solve_split(P, steps):
	maxp = max(P)
	if maxp <= 2:
		return maxp + steps
	nmax = P.count(maxp)
	if maxp == 9:
		hp = 6
		otherp = 3
	else:
		hp = maxp // 2
		otherp = maxp - hp
	newP = copy(P)
	for i in range(nmax):
		newP.remove(maxp)
	for i in range(nmax):
		newP.append(hp)
		newP.append(otherp)
	return solve(newP, steps + nmax)

def solve_step(P, steps):
	newP = [v - 1 for v in P if v > 1]
	return solve(newP, steps + 1)

def solve(P, steps):
	#print '..' * steps, P
	if not P:
		return steps
	# check splitcost
	splitcost = solve_split(P, steps)
	stepcost = solve_step(P, steps)
	#print '{}:: {}, {}'.format(steps, splitcost, stepcost)
	return min(splitcost, stepcost)


for i in range(int(raw_input())):
	print 'Case #{}:'.format(i + 1),
	D = int(raw_input())
	P = map(lambda x: int(x), raw_input().split())
	print solve(P, 0)
	
