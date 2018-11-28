#!/usr/bin/env python

import sys, pprint

T = int(sys.stdin.readline())

def solve():
	line = sys.stdin.readline().strip()
	N, M = line.split(' ')
	N = int(N)
	M = int(M)
	mtrxN = [[0 for m in range(M)] for n in range(N)]
	mtrxM = [[0 for n in range(N)] for m in range(M)]
	possibleN = [[0 for m in range(M)] for n in range(N)]
	for i in range(N):
		line = sys.stdin.readline().strip().split(' ')
		for j in range(M):
			mtrxN[i][j] = int(line[j])
			mtrxM[j][i] = int(line[j])
	for i in range(N):
		if max(mtrxN[i]) == min(mtrxN[i]):
			for j in range(M):
				possibleN[i][j] = 1

	for i in range(M):
		if min(mtrxM[i]) == max(mtrxM[i]):
			for j in range(N):
				possibleN[j][i] = 1

	done = True
	for i in range(N):
		if min(possibleN[i]) == 0:
			done = False
			break

	if done:
		return 'YES'
	
	for i in range(N):
		for j in range(M):
			if possibleN[i][j] == 0:
				curNum = mtrxN[i][j]
				if curNum == max(mtrxN[i]) or curNum == max(mtrxM[j]):
					possibleN[i][j] = 1
				else:
					return 'NO'
	return 'YES'

for t in range(T):
	result = solve()
	print "Case #%d: %s" % (t+1, result)
