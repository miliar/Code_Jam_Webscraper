#!/usr/local/bin/python

# A. 

import math
import sys
from fractions import gcd

f = sys.stdin
T = int(f.readline().strip())


# RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
def getOwp(matrix, i):
	OWP = 0.0
	ctr = 0.0
	for j in range(len(matrix)):
		if i == j: continue
		if matrix[i][j] == '.': continue
		str = matrix[j][:i] + matrix[j][i+1:]
		w = str.count('1')
		t = (len(str) - str.count('.'))
		wp = float(w)/float(t)
		OWP += wp
		ctr += 1.0

	return (OWP/ctr)

for x in range(1, T+1):
	N = int(f.readline().strip())
	matrix = []
	for n in range(N):
		matrix.append(f.readline().strip())

	wps = []
	for i in range(len(matrix)):
		wps.append(matrix[i].count('1') / float(len(matrix[i]) - matrix[i].count('.')))

	owps = []
	for i in range(len(matrix)):
		owp = getOwp(matrix, i)
		owps.append(owp)

	print "Case #%d:" % x
	for i in range(len(matrix)):
		WP = wps[i]
		OWP = owps[i]

		OOWP = 0.0
		ctr = 0.0
		for j in range(len(matrix)):
			if j == i: continue;
			if matrix[i][j] == '.': continue
			OOWP += owps[j]
			ctr += 1.0
		OOWP /= ctr

		RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
		print RPI
