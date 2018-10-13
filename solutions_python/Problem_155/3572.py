#!/bin/python3
import math

def solve(s_max, arr):
	added = 0
	count = 0
	for i in range(len(arr)):
		if i <= count:
			count += arr[i]
		else:
			to_add = i - count
			added += to_add
			count += to_add + arr[i]
	return added

num_cases = int(input())
for casenum in range(1, num_cases+1):
	s_max, arr = input().split()
	s_max = int(s_max)
	arr = list(arr)
	arr = [int(x) for x in arr]
	res = solve(s_max, arr)
	
	print ("Case #{0}: {1}".format(casenum, res))