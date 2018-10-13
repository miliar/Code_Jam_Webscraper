#!/usr/bin/env python

def test():
	numCases = int(raw_input())

	for caseNumber in range(1, numCases + 1):
		line = raw_input()
		shynessDivision = line.split()[1]
		# Max shyness.
		maxShyness = int(line.split()[0])
		# Each shyness.
		eachShyness = []
		for shynessLevel in range(maxShyness + 1):
			eachShyness.append(int(shynessDivision[shynessLevel]))

		# Code starts here.
		friendsNeeded = 0
		numStanding = eachShyness[0]
		for shynessLevel in range(1, maxShyness + 1):
			numPeopleAtThisShyness = eachShyness[shynessLevel]
			if numPeopleAtThisShyness == 0:
				continue
			if numStanding < shynessLevel:
				friendsNeeded += shynessLevel - numStanding
				numStanding += shynessLevel - numStanding
			numStanding += numPeopleAtThisShyness

		print "Case #" + str(caseNumber) + ": " + str(friendsNeeded)

test()




	








