#!/usr/bin/env python3.1

import sys

def calc():
	line = sys.stdin.readline().strip().split(" ")[1:]
	pos = {"O": 1, "B": 1}
	time = {"O": 0, "B": 0}
	for i in range(len(line)//2):
		robot = line[i*2]
		button = int(line[i*2+1])
		dist = abs(pos[robot]-button)
		pos[robot] = button
		time[robot] = 1 + max(time[robot]+dist, max(time.values()))
	return max(time.values())

numTestCases = int(sys.stdin.readline())
for i in range(numTestCases):
	result = calc()
	print("Case #%d: %d" % (i+1, result))
