#!/usr/bin/env python3.1

import sys
import fractions

def calc(great_events):
	great_events.sort()
	intervals = [great_events[i+1] - great_events[i] for i in range(len(great_events[:-1]))]
	gcd = 0
	for i in intervals: gcd = fractions.gcd(gcd, i)
	return -great_events[0] % gcd

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	result = calc(getints()[1:])
	print("Case #%d: %d" % (i+1, result))
