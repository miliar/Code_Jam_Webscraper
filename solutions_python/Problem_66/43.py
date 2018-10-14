#!/usr/bin/env python

from sys import stdin, stdout

for T in xrange(1, int(stdin.readline())+1):
	P = int(stdin.readline())
	M = map(int, stdin.readline().split())

	huge = 1000000 * P * len(M)
	y = [[huge]*(P+1) for i in xrange(len(M))]
	for i in xrange(len(M)):
		y[i][M[i]] = 0
	for i in xrange(P):
		C = map(int, stdin.readline().split())
		y2 = [[huge]*(P+1) for i in xrange(len(C))]
		for j in xrange(0, len(C)):
			for k1 in xrange(P+1):
				for k2 in xrange(P+1):
					k = min(k1, k2)
					y2[j][k] = min(y2[j][k], y[2*j][k1] + y[2*j+1][k2] + C[j])
			for k1 in xrange(P):
				for k2 in xrange(P):
					k = min(k1, k2)
					y2[j][k] = min(y2[j][k], y[2*j][k1+1] + y[2*j+1][k2+1])
		y = y2	

	stdout.write('Case #%i: %i\n' % (T, min(y[0])))

