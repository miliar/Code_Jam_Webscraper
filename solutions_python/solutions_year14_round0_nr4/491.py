#!/bin/python3

def war(n, k):
	sk = 0
	for i in range(len(n)):
		while sk < len(k) and k[sk] < n[i]:
			sk += 1
		if sk == len(k):
			return len(n) - i
		sk += 1
	return len(n) - i - 1

def dec(n, k):
	wins, sk = 0, 0
	for num in n:
		if num > k[sk]:
			wins += 1
			sk += 1
	return wins

num_cases = int(input())
for casenum in range(1, num_cases+1):
	num_blocks = int(input())
	n = sorted([float(z) for z in input().split()])
	k = sorted([float(z) for z in input().split()])
	# print(n)
	# print(k)
	print ("Case #{0}: {1} {2}".format(casenum, dec(n,k), war(n,k)))