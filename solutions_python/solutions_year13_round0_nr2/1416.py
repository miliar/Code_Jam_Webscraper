#!/usr/bin/python

import sys
# from math import sqrt, floor

DBG = False

def log(s):
	if DBG:
		print s

def p(s):
	sys.stdout.write(s)

def is_accessible(i, j, mat):
	height = mat[i][j]
	found = 0
	for row in xrange(0, h):
		if mat[row][j] > height:
			found = 1
	for col in xrange(0, w):
		if mat[i][col] > height:
			return (1 != found)
	return True

def solve(mat, w, h):
	for i in xrange(0, h):
		log("i=" + str(i))
		for j in xrange(0, w):
			log("j=" + str(j))
			if is_accessible(i, j, mat) is False:
				return "NO"
	return "YES"

n = int(raw_input())

for j in xrange(1, n+1):
	try:
		h, w = [int(_) for _ in raw_input().strip().split()]
		mat = [None] * h
		for x in xrange(0, h):
			mat[x] = [int(_) for _ in raw_input().strip().split()]
	except EOFError:
		sys.exit()

	p("Case #" + str(j) + ": ")

	p(solve(mat, w, h))

	p("\n")