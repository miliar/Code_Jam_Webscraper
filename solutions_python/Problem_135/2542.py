#! /usr/bin/env python

# python 2.7
#usage: cat input | this_program > output

import sys

num_testcases = int(sys.stdin.readline())

### main
for case in range(1, num_testcases + 1):
	n1 = int(sys.stdin.readline()) - 1
	for i in range(4):
		row = map(int, sys.stdin.readline().split())
		if i == n1:
			tip1 = set(row)
	n2 = int(sys.stdin.readline()) - 1
	for i in range(4):
		row = map(int, sys.stdin.readline().split())
		if i == n2:
			tip2 = set(row)
	candidates = tip1.intersection(tip2)
	if len(candidates) == 1:
		result = candidates.pop()
	elif len(candidates) == 0:
		result = "Volunteer cheated!"
	else:
		result = "Bad magician!"
	print "Case #%i: %s" %(case, result)
