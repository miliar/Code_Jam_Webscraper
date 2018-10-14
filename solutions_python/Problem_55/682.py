#!/usr/bin/env python

import sys

t = int(sys.stdin.readline())

for i in range(t):
	euros = 0
	line = sys.stdin.readline().split(' ');
	R, k, N = line
	queue = sys.stdin.readline().split(' ');

	for j in range(int(R)):
		free = int(k)
		for curr in range(int(N)):
			if int(queue[0]) > free:
				break
			else:
				free -= int(queue[0])
				euros += int(queue[0])
				queue.append(queue.pop(0))
	print "Case #%i: %i" % (i+1, euros)

