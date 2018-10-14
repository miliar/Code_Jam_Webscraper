#/usr/bin/python

import sys

t =  int(sys.stdin.readline())

for ii in range(t):
	x = map(int, sys.stdin.readline().split())
	n,m = x[0],x[1]
	c = [[0 for i in range(m)] for j in range(n)]
	mc = [0 for i in range(m)]
	mr = [0 for i in range(n)]

	for i in range(n):
		c[i] = map(int, sys.stdin.readline().split())
		for j in range(m):
			if (mr[i]<c[i][j]):
				mr[i] = c[i][j]
			if (mc[j]<c[i][j]):
				mc[j] = c[i][j]

	isOk = True
	for i in range(n):
		for j in range(m):
			if (c[i][j]<mr[i] and c[i][j]<mc[j]):
				isOk = False
				break
		if (not isOk):
			break
	print "Case #{0:0d}:".format(ii+1),
	if (isOk):
		print "YES"
	else:
		print "NO"
