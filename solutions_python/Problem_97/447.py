#!/usr/bin/python

import sys

T = int(sys.stdin.readline())

for k in range(0, T):
	input = sys.stdin.readline().split()
	a = int(input[0])
	b = int(input[1])
	result = 0
	while a != b:
		astr = str(a)
		count = len(astr)
		n = 1
		for i in range(0, count - 1):
			n *= 10
		t = a
		for i in range(0, count):
			t = (t % 10) * n + t / 10
			if t == a:
				break
			if t < a or t > b:
				#print "ignoring %d %d" %(a, t)
				continue
			#print "%d %d" %(a, t)
			result += 1
		a += 1
	print "Case #%d: %d" %(k + 1, result)
