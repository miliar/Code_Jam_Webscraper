#!/usr/bin/env python

import sys

def is_recycled(a, b):
	str_a, str_b = str(a), str(b)
	length = len(str_a)
	
	if length != len(str_b):
		return False
	
	for i in xrange(1, length):
		if str_a[i:] + str_a[:i] == str_b:
			return True
	
	return False

in_file = open(sys.argv[1], 'r')

num_of_cases = int(in_file.readline())
ranges = []
counts = [0 for i in xrange(num_of_cases)]

for i in xrange(num_of_cases):
	ranges.append([int(num) for num in in_file.readline().strip().split()])
	
in_file.close()

for i in xrange(num_of_cases):
	print ranges[i][0], ranges[i][1] + 1
	for n in xrange(ranges[i][0], ranges[i][1]+1):
		for m in xrange(n+1, ranges[i][1]+1):
			#print n, m
			if is_recycled(n, m):
				counts[i] += 1
				
out_file = open("result.out", 'w')

for i in xrange(num_of_cases):
	out_file.write("Case #" + str(i+1) + ": ")
	out_file.write(str(counts[i]) + '\n')
	
out_file.close()