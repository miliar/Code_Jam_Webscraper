#!/usr/bin/python

import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

re = input()
for ri in range(1, re + 1):
	h, w = map(int, raw_input().split())
	a = []
	for i in range(h):
		a.append(map(int, raw_input().split()))
	b = [[' ' for j in range(w)] for i in range(h)]
	c = chr(ord('a') - 1)
	for i in range(h):
		for j in range(w):
			if b[i][j] != ' ':
				continue
			q = [[i, j]]
			while True:
				x, y = q[-1]
				z = a[x][y]
				zz = -1
				for k in range(4):
					xx, yy = x + dx[k], y + dy[k]
					if xx >= 0 and xx < h and yy >= 0 and yy < w and a[xx][yy] < z:
						z = a[xx][yy]
						zz = k
				xx, yy = x + dx[zz], y + dy[zz]
				if zz == -1:
					c = chr(ord(c) + 1)
					break
				elif b[xx][yy] != ' ':
					c = b[xx][yy]
					break
				else:
					q.append([xx, yy])
			for x, y in q:
				b[x][y] = c
	print 'Case #' + str(ri) + ':'
	print "\n".join(map(' '.join, b))
	print >> sys.stderr, 'Case #' + str(ri) + ':'
	print >> sys.stderr, "\n".join(map(' '.join, b))

	
