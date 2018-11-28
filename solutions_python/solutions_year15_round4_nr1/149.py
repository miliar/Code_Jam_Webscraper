#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(R, C, X):
	rows = [[] for _ in range(R)]
	cols = [[] for _ in range(C)]
	for i in range(R):
		for j in range(C):
			if X[i][j] != '.':
				rows[i].append(j)
				cols[j].append(i)
	to_change = 0
	for i, row in enumerate(rows):
		for j in row:
			col = cols[j]
			if len(row)==1 and len(col)==1: return "IMPOSSIBLE"
			if X[i][j] == '<' and any(j2 < j for j2 in row): continue
			if X[i][j] == '>' and any(j2 > j for j2 in row): continue
			if X[i][j] == '^' and any(i2 < i for i2 in col): continue
			if X[i][j] == 'v' and any(i2 > i for i2 in col): continue
			to_change += 1
	return str(to_change)

T=int(input())
for test in range(T):
	R,C = [int(i) for i in input().split()]
	X = [list(input()) for _ in range(R)]
	print ('Case #%d:' % (test+1), solve(R, C, X))
