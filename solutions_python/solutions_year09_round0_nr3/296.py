#!/usr/bin/python

import sys

target = "welcome to code jam"
ntarget = len(target)

N = sys.stdin.readline().strip()

for k in range(int(N)):
	line = sys.stdin.readline().strip()
	max_x = len(line)
	max_y = len(target)
	nline = max_x

	mat = [[-1 for j in range(max_y)] for i in range(max_x)]
	i = 0
	for ch in line:
		for j in range(ntarget):
			if target[j] == ch:
				mat[i][j] = 0
		i += 1

	for i in range(nline):
		j = ntarget - 1
		if mat[i][j] == 0:
			mat[i][j] = 1

	for n in range(1,ntarget):
		j = ntarget - n - 1
		for i in range(nline):
			if mat[i][j] != -1:
				count = 0
				for i2 in range(i+1,nline):
					if mat[i2][j+1] != -1:
						count += mat[i2][j+1]
				mat[i][j] = count

	total = 0
	for i in range(nline):
		if line[i] == target[0]:
			total += mat[i][0]
	print "Case #%s: %0.4d"%(k+1,total)

