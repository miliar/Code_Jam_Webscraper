#!/usr/bin/env python

from sys import stdin

num_cases = int(stdin.readline().rstrip())

def is_possible(data, N, M):
	#print(data)
	#print(len(data))
	for i in range(len(data)):
		for j in range(len(data[i])):
			cur = data[i][j]
			#print i, j
			#print cur
			vert = False
			hor = False
			for k in range(len(data[i])):
				if data[i][k] > cur:
					vert = True
			for l in range(len(data)):
				if data[l][j] > cur:
					hor = True
			if vert and hor:
				return "NO"
	return "YES"

for case in range(num_cases):
	dim = stdin.readline().rstrip().split(" ")
	N = int(dim[0])
	M = int(dim[1])

	data = []
	for row in range(N):
		data.append(map(int, stdin.readline().rstrip().split(" ")))

	possible = is_possible(data, N, M)

	#for line in data:
	#	print " ".join(map(str, line))

	print "Case #{}: {}".format(case + 1, possible)
