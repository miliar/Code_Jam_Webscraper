#!/usr/bin/python
import re
import sys


header = sys.stdin.readline().rstrip()
l, d, n = header.split(' ')


lines = sys.stdin.readlines()

dictionary = []
tests = []

l = int(l)
d = int(d)
n = int(n)

for line in lines:
	line = line.rstrip()
	if d > 0:
		dictionary.append(line)
		d = d - 1
	elif d == 0 and n > 0:
		tests.append(line)
		n = n - 1
		
sofar = 1
		
for test in tests:
	example = test.replace('(','[')
	example = example.replace(')',']')
	c = 0
	for item in dictionary:
		if re.match(example, item) != None:
			c = c + 1
	print "Case #%d: %d" % (sofar, c)
	sofar = sofar + 1
		
