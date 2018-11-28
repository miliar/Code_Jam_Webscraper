#!/usr/bin/python

import sys

def choose(mat, i, j, w, h):
	alt = []
	if (i-1) < 0: #north 0
		alt.append(999999)
	else:
		alt.append(mat[i-1][j])

	if (j-1) < 0: #west 1
		alt.append(999999)
	else:
		alt.append(mat[i][j-1])

	if (j+1) >= h: #east 2
		alt.append(999999)
	else:
		alt.append(mat[i][j+1])

	if (i+1) >= w: #south 3
		alt.append(999999)
	else:
		alt.append(mat[i+1][j])

	mv = min(alt)
	if mv >= mat[i][j]:
		return 4 # don't flow
	else:
		malt = alt.index(mv)
		return malt

count = 0
def drain(mat,sinkmat,i,j):
	global count
	if sinkmat[i][j] == -1:
		d = choose(mat,i,j,w,h)
		if d == 0:
			drain(mat,sinkmat,i-1,j)
			sinkmat[i][j] = sinkmat[i-1][j]
		elif d == 1:
			drain(mat,sinkmat,i,j-1)
			sinkmat[i][j] = sinkmat[i][j-1]
		elif d == 2:
			drain(mat,sinkmat,i,j+1)
			sinkmat[i][j] = sinkmat[i][j+1]
		elif d == 3:
			drain(mat,sinkmat,i+1,j)
			sinkmat[i][j] = sinkmat[i+1][j]
		elif d == 4:
			sinkmat[i][j] = count
			count += 1
	else:
		pass

T = sys.stdin.readline().strip()
for t in range(int(T)):
	count = 0
	(w,h) = sys.stdin.readline().strip().split(" ")
	w = int(w)
	h = int(h)
	mat = [[0 for j in range(h)] for i in range(w)]
	mat[0][0] = 1	
	for i in range(w):
		line = sys.stdin.readline().strip()
		j = 0
		for v in line.split(" "):
			mat[i][j] = int(v)
			j += 1

	sinkmat = [[0 for j in range(h)] for i in range(w)]

	for i in range(w):
		for j in range(h):
			sinkmat[i][j] = -1
	for i in range(w):
		for j in range(h):
			drain(mat,sinkmat, i,j)	
	print "Case #%s:"%(t+1)
	for i in range(w):
		for j in range(h):
			sys.stdout.write(chr(97+sinkmat[i][j]) + " ")
		print


