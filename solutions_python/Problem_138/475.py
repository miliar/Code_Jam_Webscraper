#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(Naomi, Ken):
	Naomi.sort()
	Ken.sort()
	pts_dw, pts_war = 0, 0
	N_lo, N_hi = 0, len(Naomi)-1
	K_lo, K_hi = 0, len(Ken)-1

	while N_lo <= N_hi:
		if Naomi[N_lo] < Ken[K_lo]:
			K_hi -= 1
		else:
			K_lo += 1
			pts_dw += 1
		N_lo += 1

	N_lo, N_hi = 0, len(Naomi)-1
	K_lo, K_hi = 0, len(Ken)-1

	while N_lo <= N_hi:
		if Naomi[N_hi] > Ken[K_hi]:
			pts_war += 1
			K_lo += 1
		else:
			K_hi -= 1
		N_hi -= 1

	return pts_dw, pts_war

if __name__ == "__main__":
	T = int(raw_input())
	for i in xrange(1, T+1):
		N = int(raw_input())
		Naomi = map(float, raw_input().split())
		Ken = map(float, raw_input().split())
		dw, war = solve(Naomi, Ken)
		print "Case #%d: %d %d" % (i, dw, war)
