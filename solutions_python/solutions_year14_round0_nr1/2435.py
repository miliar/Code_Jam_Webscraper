#!/usr/bin/env python

import sys

FILE = sys.stdin

def setForCase():
	rowa = int(FILE.readline())
	for skip in range(rowa-1):
		FILE.readline()
	setr = set([int(x) for x in (FILE.readline()).strip().split(' ')])
	for skip in range(4 - rowa):
		FILE.readline()
	return setr

if len(sys.argv) > 1:
	FILE = open(sys.argv[1])

cases = int(FILE.readline())

for case in range(cases):
	setIntersection = setForCase() & setForCase()
	if len(setIntersection) == 0:
		print("Case #"+str(case+1)+": "+"Volunteer cheated!")
	elif len(setIntersection) == 1:
		print("Case #"+str(case+1)+": "+str(setIntersection.pop()))
	else:
		print("Case #"+str(case+1)+": "+"Bad magician!")

