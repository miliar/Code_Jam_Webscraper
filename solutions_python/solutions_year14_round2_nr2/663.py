#!/usr/bin/python

import sys

input_file = open(sys.argv[1])

cases = int(input_file.readline())

for case in xrange(cases):
	print 'Case #%d:' % (case+1,),

	a, b, k = (int(x) for x in input_file.readline().split())

	sum = 0

	for x in xrange(a):
		for y in xrange(b):
			if x&y < k:
				sum = sum + 1

	print sum

input_file.close()
