#!/usr/bin/python
import sys

T = int(sys.stdin.readline())

for i in xrange(T):
	N, M = sys.stdin.readline().split()
	N, M = int(N),int(M)
	A = []
	for x in xrange(N):
		A.append(sys.stdin.readline().strip('\n'))
		A[x] = A[x].split()
		A[x] = map(int, A[x])

	for x in xrange(M):
		if A[0][x] <= 1 and A[N-1][x] <= 1:
			for y in xrange(N):
				if not A[y][x] <= 1:
					break
			else:
				for y in xrange(N):
					A[y][x] = 0
	for x in xrange(N):
		if A[x][0] <= 1 and A[x][M-1] <= 1:
			for y in xrange(M):
				if not A[x][y] <= 1:
					break
			else:
				for y in xrange(M):
					A[x][y] = 0
	flag = 0
	for x in A:
		for y in x:
			if y == 1:
				flag = 1
				break
	if flag == 1:
		print 'Case #%d: NO' %(i+1)
	else:
		print 'Case #%d: YES' %(i+1)

							