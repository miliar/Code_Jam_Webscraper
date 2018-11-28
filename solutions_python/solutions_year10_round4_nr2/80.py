#!/usr/bin/env python3.1

import sys

def calc(rounds, teamdata):
	required = [max(0,rounds - x) for x in teamdata]
	return tickets(required)

def tickets(required):
	if max(required) == 0:
		return 0
	else:
		required = [max(0,x-1) for x in required]
		mid = len(required) // 2
		return 1 + tickets(required[:mid]) + tickets(required[mid:])

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	numRounds = getints()[0]
	result = calc(numRounds, getints())
	for x in range(numRounds): getints()
	print("Case #%d: %d" % (i+1, result))
