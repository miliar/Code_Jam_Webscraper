#!/usr/bin/env python
# Google Code Jam 2011
# Qualification round
# Jeremy Chin <rekless@gmail.com>
# Bot Trust

import math
import sys


f = open(sys.argv[1])

time = [0,0]
position = [1,1]

def press(bot, location):
	diff = abs(location - position[bot])
	time[bot] += 1 + diff # 1s to press button
	position[bot] = location
	ot = time[bot^1]
	if ot >= time[bot]:
		time[bot] = ot + 1
	return time[bot]

def bot(c):
	if c == "O":
		return 0
	return 1
		

def process(line):
	for i in range(0, len(line)/2):
		time = press(bot(line[i*2]), int(line[i*2+1]))
	return time

f.readline()
idx = 1
for line in f:
	time = [0,0]
	position = [1,1]
	time = process(line.split()[1:])
	print "Case #%s: %s" % (idx, time)
	idx += 1

