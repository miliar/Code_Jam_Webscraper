#! /usr/bin/python

from math import ceil, floor

T = int(raw_input())

def minServ(exact):
	return ceil(exact/1.1)

def maxServ(exact):
	return floor(exact/0.9)

for t in range(1, T+1):

	N, P = [int(inp) for inp in raw_input().split()]
	recipe = [int(inp) for inp in raw_input().split()]
	values = [sorted([int(inp) for inp in raw_input().split()]) for _ in range(N)]
	portions = [[(1.0 * values[i][j]) / recipe[i] for j in range(P)] for i in range(N)]
	minPortions = [[minServ(portions[i][j]) for j in range(P)] for i in range(N)]
	maxPortions = [[maxServ(portions[i][j]) for j in range(P)] for i in range(N)]

	index = [0]*N
	servings = 0

	while all([index[i] < P for i in range(N)]):
		maxPortion = min([maxPortions[i][index[i]] for i in range(N)])
		minPortion = max([minPortions[i][index[i]] for i in range(N)])

		if maxPortion < minPortion:
			minInd = 0
			for i in range(N):
				if portions[i][index[i]] < portions[minInd][index[minInd]]:
					minInd = i
			index[minInd] += 1
		else:
			servings += 1
			for i in range(N):
				index[i] += 1

	print 'Case #' + str(t) + ': ' + str(servings)
