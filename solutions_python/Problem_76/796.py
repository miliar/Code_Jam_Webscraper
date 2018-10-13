#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())

for t in range(T):
	N = int(sys.stdin.readline())
	line = [int(x) for x in sys.stdin.readline().split()]
	result = 0

	for n in range(N):
		result = result ^ int(line[n])

	if result == 0:
		result = sum(line) - min(line)
	else:
		result = 'NO'

	print 'Case #%s: %s' % (t+1, result)
