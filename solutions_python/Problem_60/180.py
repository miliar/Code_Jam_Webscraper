#!/usr/bin/python

from __future__ import division

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())
	testCases = []

	for testCase in xrange(testCaseCount):
		n, k, b, t = [int(x) for x in file.readline().rstrip().split()]

		Xs = [int(x) for x in file.readline().rstrip().split()]
		Vs = [int(x) for x in file.readline().rstrip().split()]

		testCases.append((n, k, b, t, Xs, Vs))
	
	return testCases

def solve((n, k, b, t, Xs, Vs)):
	"""
	k: chicks needed
	b: distance from 0 to barn
	t: max time
	Xs: position of chicks
	Vs: velocity of chicks
	"""

	# find the time of arrival
	arrivalTimes = [((b - Xs[i]) / Vs[i]) for i in xrange(n)]
	arrivals = [i for i in xrange(n) if arrivalTimes[i] <= t]
	
	if len(arrivals) < k:
		return 'IMPOSSIBLE'

	# first look at the chicks in front
	arrivals.reverse()

	swaps = [0] * n
	
	chickCount = 0

	for thisChick in arrivals:
		for otherChick in xrange(n):
			# only consider chicks in front
			if not otherChick > thisChick:
				continue

			# only consider chicks slower than this chick
			if arrivalTimes[otherChick] <= arrivalTimes[thisChick]:
				continue

			distance = Xs[otherChick] - Xs[thisChick]
			speedDifference = Vs[thisChick] - Vs[otherChick]
			timeAtEncounter = distance / speedDifference
			positionAtEncounter = Xs[thisChick] + (timeAtEncounter * Vs[thisChick])
			distanceRemaining = b - positionAtEncounter
			timeRemaining = distanceRemaining / Vs[otherChick]
			timeAtOtherChickSpeedFromHere = timeAtEncounter + timeRemaining

			if timeAtOtherChickSpeedFromHere <= t:
				# chick in front is fast enough
				# add their swaps and stop
				swaps[thisChick] += swaps[otherChick]
				break

			# chick in front is too slow. Swap!
			swaps[thisChick] += 1

		chickCount += 1

		if chickCount == k:
			break

	return sum(swaps)

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
