#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Do you ever become frustrated with television because you keep
seeing the same things, recycled over and over again? Well I
personally don't care about television, but I do sometimes feel that way
about numbers.

Let's say a pair of distinct positive integers (n, m) is recycled if you can
obtain m by moving some digits from the back of n to the front without changing
their order. For example, (12345, 34512) is a recycled pair since you can
obtain 34512 by moving 345 from the end of 12345 to the front. Note that
n and m must have the same number of digits in order to be a recycled pair.
Neither n nor m can have leading zeros.

Given integers A and B with the same number of digits and no leading zeros,
how many distinct recycled pairs (n, m) are there with A ≤ n < m ≤ B?'''
import sys

sys.stdin.next()

def recycled(a, b):
	'''a is recycled from b if the digits are in the same order when cycled'''
	a = str(a)
	b = str(b)

	l = len(a)
	for i in xrange(l):
		if a[i:] + a[:i] == b:
			return True
	return False

def num_recycled_pairs(start, end):
	'''Count the number of recycled pairs within a range'''
	total = 0
	for m in xrange(start + 1, end + 1):
		for n in xrange(start, m):
			if recycled(m, n):
				total += 1
	return total

for case, line in enumerate(sys.stdin):
	a, b = line.split()
	output = num_recycled_pairs(int(a), int(b))

	print 'Case #%d: %d' % (case+1, output)
