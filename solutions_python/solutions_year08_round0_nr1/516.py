#!/usr/bin/python

import re, sys

sys.setrecursionlimit(1500)

num = re.compile("^(\d*)$")

def findswitches(engines, queries):
	global switches
	
	l = [0] * len(engines)
	for i in range(len(engines)):
		for q in queries:
			if engines[i] == q:
				break
			l[i] += 1
			
	if max(l) < len(queries):
		switches += 1
		findswitches(engines, queries[max(l):])

f = open("test.txt")

cases = int(f.readline())

lines = f.readlines()
c = 0
case = 1

for i in range(len(lines)):
	m = num.match(lines[i])
	if m:
		n = int(m.group(1))
		if c == 0:
			engines = lines[i + 1 :i + n + 1]
			c = 1
		elif c == 1:
			queries = lines[i + 1 :i + n + 1]
			switches = 0
			findswitches(engines, queries)
			print "Case #%d: %d" % (case, switches)
			case += 1
			c = 0