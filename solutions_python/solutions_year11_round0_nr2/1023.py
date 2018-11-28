#!/usr/bin/python

import sys

def solve(combine, opposed, elements):
	l = ''
	combineMap = dict()
	for c in combine:
		combineMap[c[0]+c[1]] = c[2]
		combineMap[c[1]+c[0]] = c[2]
	opposedMap = dict()
	for o in opposed:
		opposedMap[o[0]] = o[1]
		opposedMap[o[1]] = o[0]
	for e in elements:
		# print(elements)
		# print(e)
		l = l + e
		if len(l) > 1 and (l[-2]+l[-1]) in combineMap:
			l = str(l[0:-2]) + str(combineMap[ (l[-2]+l[-1]) ])
		if l[-1] in opposedMap:
			opposedChar = opposedMap[l[-1]]
			index = l.find(opposedChar)
			if index >= 0:
				l = ''
	output = ''
	for c in l:
		if len(output) > 0:
			output += ', '
		output += c
	return '[' + output + ']'

f = open(sys.argv[1], "r")
cases = int(f.readline())
for case in range(1, cases+1):
	line = f.readline().split()
	i = 0
	c = int(line[i])
	i += 1
	combine = []
	while len(combine) < c:
		combine.append(line[i])
		i += 1
	d = int(line[i])
	i += 1
	opposed = []
	while len(opposed) < d:
		opposed.append(line[i])
		i += 1
	n = int(line[i])
	i += 1
	elements = line[i]
	assert(n == len(elements))
	print("Case #%d: %s" % (case, solve(combine, opposed, elements)))
