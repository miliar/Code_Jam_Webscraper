#!/usr/bin/python
import sys
from fractions import Fraction

infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())
caseNum = 0

for case in range(numCases):
	caseNum += 1
	nums = [int(i) for i in infile.readline().split()]
	N = nums[0]
	D = nums[1]
	G = nums[2]
	
	a = Fraction(D, 100)
	
	if G == 100 and D != 100:
		print "Case #%s: Broken" % caseNum
	elif a.denominator > N:
		print "Case #%s: Broken" % caseNum
	elif G == 0 and D != 0:
		print "Case #%s: Broken" % caseNum
	else:
		print "Case #%s: Possible" % caseNum
