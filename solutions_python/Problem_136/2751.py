#!/usr/bin/python

import sys

def cal(c, f, x):
	prev = x / 2
	common = c/2
	current = common + x / (f+2)

#	print prev, current
	const = 2

	while prev > current:
		prev = current
		current = common

		current = current + c / ((const-1)*f+2)

		common = current

		current = current + x / (const*f+2)

		const = const + 1

#		print 'current =', current

	return prev

input_file = open(sys.argv[1])

cases = int(input_file.readline())

for case in xrange(cases):
	print 'Case #'+str(case+1)+':',

	c, f, x = [float(x) for x in input_file.readline().split(' ')]

	print '%.7f' % (cal(c, f, x),)

input_file.close()
