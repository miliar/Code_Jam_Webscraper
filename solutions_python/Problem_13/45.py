#!/usr/bin/python

import sys

def min(x, y):
	if x > y:
		return y
	return x

def solveTree(arr, tree, result, i = 1):
	if arr[i][result] != -1:
		return arr[i][result]
	
	if tree[i][1] == -1:
		if tree[i][0] == result:
			return 0
		else:
			return float("infinity")

	c00 = solveTree(arr, tree, 0, 2 * i)
	c10 = solveTree(arr, tree, 0, 2 * i + 1)
	c01 = solveTree(arr, tree, 1, 2 * i)
	c11 = solveTree(arr, tree, 1, 2 * i + 1)
	
	if result == 0:
		cAnd = min(c00 + c10, min(c00 + c11, c01 + c10))
		cOr = c00 + c10
	else:
		cAnd = c11 + c01
		cOr = min(c01 + c11, min(c01 + c10, c00 + c11))

	if tree[i][0] == 1:
		if tree[i][1] == 0:	
			arr[i][result] = cAnd
		else:
			arr[i][result] = min(cAnd, cOr + 1)
	else:
		if tree[i][1] == 0:
			arr[i][result] = cOr
		else:
			arr[i][result] = min(cOr, cAnd + 1)

	return arr[i][result]

if len(sys.argv) < 2:
	print "oops"
	sys.exit(1)

f = open(sys.argv[1], "r")

numCases = int(f.readline())

for c in range(numCases):
	line = f.readline().split()
	m = int(line[0])
	
	arr = [[-1 for i in range(2)] for j in range(m + 1)]

	result = int(line[1])

	tree = [[-2, -2] for i in range(m + 1)]

	for i in range((m - 1) / 2):
		line = f.readline().split()
		tree[i + 1][0] = int(line[0])
		tree[i + 1][1] = int(line[1])

	for i in range((m - 1) / 2, m):
		line = f.readline()
		tree[i + 1][0] = int(line)
		tree[i + 1][1] = -1

	r = solveTree(arr, tree, result)

	if r == float("infinity"):
		print "Case #" + str(c + 1) + ": IMPOSSIBLE"
	else:
	 	print "Case #" + str(c + 1) + ": " + str(r)

