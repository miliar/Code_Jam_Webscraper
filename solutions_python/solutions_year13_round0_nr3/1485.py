#!/usr/bin/env python

from sys import argv
from math import pow, sqrt

if len(argv) != 2:
	print 'Usage: %s filename' % argv[0]
	exit()

inp = []

with open(argv[1]) as f:
	for line in f:
		inp.append(line[:-1])

T = int(inp.pop(0))

for i in range(len(inp)):
	inp[i] = inp[i].split(' ')
	for j in range(len(inp[i])):
		inp[i][j] = int(inp[i][j])

def is_palindrome(n):
	n = str(n)
	return n == n[::-1]

count = 1
for case in inp:
	A = case[0]
	B = case[1]

	n = 0
	i = int(sqrt(A))

	while i*i <= B:
		if is_palindrome(i):
			if is_palindrome(i*i):
				if A <= i*i and i*i <= B:
					n += 1
		i += 1

	print "Case #%s: %s" % (count, n)
	count += 1
