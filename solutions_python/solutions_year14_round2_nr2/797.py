#!/usr/bin/env python

import io

def get_ones(arr, pos):
	count = 0
	for it in arr:
		if it[pos] == '1':
			count = count + 1

	return count

f = open("input.txt")

cases = int(f.readline())

for case_n in range(cases):

	[a, b, k] = [int(num) for num in f.readline().rstrip().split(" ")]

	count = 0
	for i in range(0, a):
		for j in range(0, b):
			count = count + ((i & j) < k)
		
	print "Case #%d: %d" % ((case_n + 1), count)
