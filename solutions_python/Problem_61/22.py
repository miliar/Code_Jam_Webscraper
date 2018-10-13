#!/usr/bin/python
# Author: Ivan Kazmenko
import sys
tests = int (sys.stdin.readline ())
MaxN = 501
MOD = 100003

c = [[0 for i in range (MaxN)] for j in range (MaxN)]
for i in range (MaxN):
	c[i][0] = 1
	for j in range (1, i + 1):
		c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD

f = [[0 for i in range (MaxN)] for j in range (MaxN)]
for i in range (2, MaxN):
	f[i][1] = 1
	for j in range (2, i):
		for k in range (1, j):
			f[i][j] += (c[i - j - 1][j - k - 1] * f[j][k]) % MOD

for test in range (tests):
	n = int (sys.stdin.readline ())
	sys.stdout.write ('Case #%d: %d\n' % (test + 1, sum (f[n]) % MOD))
