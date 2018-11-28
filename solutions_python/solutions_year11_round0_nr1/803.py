#!/usr/bin/python
# Python 2.6.5
# Google Code Jam 2011: Problem A (Bot Trust)

import sys

T = int(sys.stdin.readline())
for case in xrange(1,T+1):
	line = sys.stdin.readline().split()
	pos = {'O':1, 'B':1}
	storage = 0
	time = 0
	cur = 'O'
	for button in range(int(line[0])):
		colour = line[2*button+1]
		place = int(line[2*button+2])
		if colour == cur:
			usage = abs(place - pos[colour]) + 1
		else:
			usage = max(0, abs(place-pos[colour]) - storage) + 1
			cur = colour
			storage = 0
		storage += usage
		time += usage
		pos[colour] = place
	print "Case #{0}: {1}".format(case, time)
	
		
