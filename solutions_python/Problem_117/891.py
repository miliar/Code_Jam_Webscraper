#!/usr/bin/python

import numpy as np

def transpose(l, N, M):
	if N == M:
		return [[l[j][i] for j in range(M)] for i in range(N)]
	else:
		return [[l[j][i] for j, c in enumerate(row)] for i, row in enumerate(np.zeros([M, N]))]

def printl(lawn):
	for l in lawn:
		print l
	print

def mow_horizontal(lawn, goal_lawn, N, M):
	for i in range(N):
		height = max(goal_lawn[i])
		for j in range(M):
			if lawn[i][j] > height:
				lawn[i][j] = height

def check(goal_lawn, N, M):
	lawn = [[100 for j in range(M)] for i in range(N)]

	print 'Initial lawn'
	printl(lawn)

	mow_horizontal(lawn, goal_lawn, N, M)
	
	lawn = transpose(lawn, N, M)
	goal_transp = transpose(goal_lawn, N, M)
	
	mow_horizontal(lawn, goal_transp, M, N)

	lawn = transpose(lawn, M, N)

	print 'Final lawn'
	printl(lawn)

	if lawn == goal_lawn:
		return 'YES'
	else:
		return 'NO'

fp = open('B-large.in')
fpout = open('output.txt', 'w')
cases = int(fp.readline())

for i in range(cases):
	[N, M] = [int(c) for c in fp.readline().split()]
	goal_lawn = [[int(c) for c in fp.readline().split()] for j in range(N)]
	
	print 'Goal'
	printl(goal_lawn)

	result = check(goal_lawn, N, M)
	print result
	print
	
	fpout.write('Case #%d: %s\n' %(i+1, result))