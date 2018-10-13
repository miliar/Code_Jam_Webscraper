#!/usr/bin/python

debugOutput = False

maxTestCases = int(raw_input())

if(debugOutput):
	print maxTestCases

for testCase in xrange(1, maxTestCases+1):
	radius, paint = map(long, raw_input().split(' '))

	if(debugOutput):
		print "{} {}".format(radius,  paint)

	numOfRings = 0

	radInc = 1
	while(paint > 0):
		paint = paint - ((2 * radius) + (radInc + (radInc-1)))
		if(paint < 0):
			break;
		numOfRings += 1
		radInc += 2

	print "Case #{}: {}".format(testCase, numOfRings)



