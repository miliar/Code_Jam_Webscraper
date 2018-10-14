#!/usr/bin/python
import sys

T = int(sys.stdin.readline())
for t in range(T):
	N,M = [int(x) for x in sys.stdin.readline().split()]
	
	L = []
	mark = [[False for i in range(M)] for j in range(N)]
	for n in range(N):
		L.append([int(x) for x in sys.stdin.readline().split()])
	
	for i in range(N):
		m = max(L[i])
		for j in range(M):
			if L[i][j] == m:
				mark[i][j] = True
	for i in range(M):
		ma = L[0][i]
		for j in range(1, N):
			ma = max(ma, L[j][i])
		for j in range(N):
			if L[j][i]==ma:
				mark[j][i] = True
	P = True
	for i in range(N):
		for j in range(M):
			if mark[i][j]==False:
				P = False
				break
		if P==False:
			break
	print "Case #%d: %s" % (t + 1, P and "YES" or "NO")
			
		
