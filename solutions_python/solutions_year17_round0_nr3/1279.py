import sys
import math

n = int(input())
for k in range(n):
	N, K = [int(i) for i in input().split()]
	ncuts = 0
	currentpart = 1
	part = {}
	part[N] = 1
	largepart = 0
	Ls = 0
	Rs = 0
	for i in range(K):
		largepart = max(part.keys())
		part[largepart] -= 1
		if (part[largepart] == 0):
			part.pop(largepart)
		if (largepart % 2 == 1):
			if (largepart//2 in part):
				part[largepart//2] += 2
			else:
				part[largepart//2] = 2
			Ls = largepart//2
		else:
			if (largepart//2 in part):
				part[largepart//2] += 1
			else:
				part[largepart//2] = 1
			if ((largepart//2 -1) in part):
				part[(largepart//2 -1)] += 1
			else:
				part[(largepart//2 -1)] = 1
			Ls = (largepart//2 - 1)
		Rs = largepart //2 
	print("Case #" + str(k+1) + ": " + str(int(Rs)) + " " + str(int(Ls)))