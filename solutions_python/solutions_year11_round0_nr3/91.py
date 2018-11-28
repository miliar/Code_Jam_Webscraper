#!/usr/bin/env python3.1

import sys
from functools import reduce

def calc(values):
	def xor(a, b): return a ^ b
	if reduce(xor, values) != 0: return "NO"
	return str(sum(values) - min(values))

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	sys.stdin.readline()
	result = calc(getints())
	print("Case #%d: %s" % (i+1, result))
