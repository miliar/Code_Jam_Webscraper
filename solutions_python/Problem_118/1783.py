#!/usr/bin/env python
def is_pal(x):
	r=str(x)
	return r == r[::-1]

import sys
import math

def readint():
	return map(int, sys.stdin.readline().strip().split())

t, = readint()

def test():
	a,b = readint()

	wy=0

	for i in range(a,b+1):
		x = int(math.sqrt(i))
		if is_pal(i) and is_pal(x) and x*x ==i:
			wy+=1
	return wy

for i in range(1,t+1):
	print("Case #{}:".format(i), test())
