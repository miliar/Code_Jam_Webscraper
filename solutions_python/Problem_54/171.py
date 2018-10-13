#!/usr/local/bin/python3.1
from fractions import gcd

x = [[int(n) for n in line.strip().split()] for line in open('B-large.in', 'r').readlines()]
# get rid of meta info
T = x[0][0]

for t in range(1, T + 1):
	row = x[t]
	N = row[0]
	diffs = []
	for i in range (1, N + 1):
		for j in range (i + 1, N + 1):
			diffs.append(abs(row[i] - row[j]))
	# diffs contains at least one element (as N is at least 2)
	gc = diffs[0];
	for d in diffs[1:]:
		gc = gcd(gc, d)
	if (row[1] % gc) == 0:
		ans = 0
	else:
		ans = gc - (row[1] % gc)
	print('Case #{0}: {1}'.format(t, ans))
