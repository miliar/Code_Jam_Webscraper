#!/usr/bin/env python3.1

import sys
from math import ceil, log

def calc(a, b, c):
	p = log((log(b)-log(a))/log(c))
	p -= 1e-15 #compensate for rounding errors
	return max(0,ceil(p/log(2)))

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	args = getints()
	result = calc(args[0], args[1], args[2])
	print("Case #%d: %s" % (i+1, result))
