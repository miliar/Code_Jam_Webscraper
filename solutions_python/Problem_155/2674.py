#!/bin/python

with open ("A-large.in", "r") as myfile:
    inStr=myfile.read()

lines = inStr.splitlines();
lines = lines[1:]

for testCase in xrange(0,len(lines)):
	s1 = lines[testCase].split()
	# print "Max Shyness " + s1[0]
	# print "Num People " + s1[1]

	s1[0] = int(s1[0])


	shynessLevels = [0]*(s1[0]+1)
	for shyLevel in xrange(0,len(s1[1])):
		shynessLevels[shyLevel] = int(s1[1][shyLevel])

	# print shynessLevels

	totalStanding = 0
	extras = 0
	for shyLevel in xrange(0,s1[0]+1):
		# print "shyLevel: " + str(shyLevel) + " totalStanding: " + str(totalStanding)
		if shyLevel > totalStanding:
			#need extra person(s)
			# print "adding extra"
			diff = shyLevel - totalStanding
			extras += diff
			totalStanding += diff
		
		totalStanding += shynessLevels[shyLevel]

	# print "Need " + str(extras) + " extras"

	print "Case #" + str(testCase+1) + ":", str(extras)