#!/usr/bin/env python3

import sys
import math
import copy

lines = [ l.strip() for l in sys.stdin.readlines() ]
T = int(lines[0])
L = 1

def check(h, heights):
	res = 0
	for i in range(len(heights)):
		if heights[i] <= h: continue
		for j in range(i):
			if heights[i] <= h: break
			rem = min(heights[i] - heights[j], heights[i] - h)
			#print("Sposto %d su %d" % (rem, j))
			heights[i] -= rem
			heights[j] += rem
			res += rem
		if heights[i] > h:
			#print("fail ", heights)
			return -1
	return res

for t in range(T):
	N, C, M = map(int, lines[L].split(' '))
	L += 1

	heights = [0] * N
	rep = [0] * C

	for i in range(M):
		pos, cus = map(int, lines[L].split(' '))
		pos -= 1
		cus -= 1
		L += 1
		heights[pos] += 1
		rep[cus] += 1

	low = max(rep)
	hi = M
	#print("low %d hi %d" % (low, hi))
	while low < hi:
		mid = (low + hi) // 2
		if check(mid, copy.deepcopy(heights)) >= 0:
			hi = mid
		else:
			low = mid + 1

	cost = check(low, copy.deepcopy(heights))
	print("Case #%d: %d %d" % (t+1, low, cost))
