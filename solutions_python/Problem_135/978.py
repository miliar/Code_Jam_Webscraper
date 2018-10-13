#!/usr/bin/python

import sys

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
	ans1=int(caseInput)
	for line in xrange(1,5):
		rowtxt=sys.stdin.readline()
		if ans1==line:
			row1=set(rowtxt.split())
	caseInput=sys.stdin.readline()
	ans2=int(caseInput)
	for line in xrange(1,5):
		rowtxt=sys.stdin.readline()
		if ans2==line:
			row2=set(rowtxt.split())

	l=len(row1.intersection(row2))
	if l == 0:
		print "Case #"+str(case)+": Volunteer cheated!"
	if l == 1:
		print "Case #"+str(case)+": "+row1.intersection(row2).pop()
	if l > 1:
		print "Case #"+str(case)+": Bad magician!"

	# *** END CODE READING CASE ***

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

