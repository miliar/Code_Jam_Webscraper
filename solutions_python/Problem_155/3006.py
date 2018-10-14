#! /usr/bin/python

maxTests = -1
debug = False

if __name__ == "__main__":
	maxTests = int(raw_input())
	if debug: print "--- Max Test Cases: %s" % maxTests

	for testCase in xrange(1,maxTests+1):
		shyMax = None # How many standing by the time you reach this level
		audience = None
		friends = 0
		currStanding = 0

		(shyMax, audience) = raw_input().split()
		shyMax = int(shyMax)

		if debug: print "--- %s %s" % (shyMax, audience)

		shyLevel = 0
		while (shyMax > (currStanding + friends)) or (shyLevel < shyMax):
			shyPeople = int(audience[shyLevel])

			if debug: print "--- LEVEL %d : PEOPLE %d : CURSTANDING %d : FRIENDS %d" % (shyLevel, shyPeople, currStanding, friends)

			if shyLevel > (currStanding+friends):
				friends += shyLevel - (currStanding+friends)

			currStanding += shyPeople


			shyLevel += 1
		
		print "Case #%d: %s" % (testCase, friends)
