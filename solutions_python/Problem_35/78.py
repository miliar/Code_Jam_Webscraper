#!/usr/bin/python
import sys
		
def readints():
	return map(int, sys.stdin.readline().split())
	

T = int(sys.stdin.readline())
for cs in range(1, T+1):
	H, W = readints()
	alt = []
	res = []
	for i in range(H):
		alt.append(readints())
		assert(len(alt[-1]) == W)
		res.append([None] * W)
		
	nbasins = 0
	
	def valid(i, j):
		return 0 <= i < H and 0 <= j < W
		
	def dfs(i, j):
		global alt, res, nbasins
		assert valid(i,j)
		if res[i][j] is not None: return res[i][j]
		
		dy = [-1,  0, 0, 1]
		dx = [ 0, -1, 1, 0]
		
		iii = i
		jjj = j
		
		for d in range(4):
			ii = i + dy[d]
			jj = j + dx[d]
			if not valid(ii, jj): continue
			if alt[ii][jj] < alt[iii][jjj]:
				iii = ii
				jjj = jj
				
		if iii == i and jjj == j:
			nbasins += 1
			res[i][j] = chr(ord('a') + nbasins - 1)
		else:
			res[i][j] = dfs(iii, jjj)
		return res[i][j]


	for i in range(H):
		for j in range(W):
			dfs(i, j)

	print "Case #%d:" % cs
	for i in range(H):
		print ' '.join(res[i])

