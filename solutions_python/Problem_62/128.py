#!/usr/bin/env python3.1

import sys

def calc(wires):
	i = 0
	for i1 in range(len(wires)):
		for i2 in range(len(wires[:i1])):
			w1 = wires[i1]
			w2 = wires[i2]
			if (w1[0] < w2[0]) == (w1[1] > w2[1]):
				i += 1
	return i

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	numWires = getints()[0]
	wires = []
	for w in range(numWires):
		wires.append(getints())
	result = calc(wires)
	print("Case #%d: %d" % (i+1, result))
