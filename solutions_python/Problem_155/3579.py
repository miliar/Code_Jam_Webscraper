#Google code jam 2015
# Task 1. Prima Dona. 

import sys
import string as str

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

inputFile = open(inputFileName, 'r')
n = int(inputFile.readline()) #number of test cases



outputFile = open(outputFileName, 'w')


# if v == 0:
# 	print 'blah'
# elif v == 5:
# 	print 'blahbalh'
# else:
# 	print 'blaaaaah'

for i in range (n): #number of test cases
	(shiest, audience) = str.split(inputFile.readline())
	shiest = int(shiest)

	currentlyStanding = 0
	friendsInvited = 0
	print "Case #", i
	print "shiest = ", shiest
	print "audience = ", audience
	for j in range (shiest + 1):
		print "audience = ", audience[j]
		if int(audience[j]) == 0:
			continue

		if j == 0:
			print 'currentlyStanding = ', currentlyStanding + int(audience[j])
			currentlyStanding += int(audience[j])

		elif currentlyStanding >= j:
			print 'enough standing'
			print 'currentlyStanding = ', currentlyStanding + int(audience[j])
			currentlyStanding += int(audience[j])
			#print 'blahbalh'
		else:
			#print 'blaaaaah'
			print 'not enough standing'
			print 'invite friends = ', j - currentlyStanding
			print 'currentlyStanding = ', currentlyStanding + int(audience[j]) + friendsInvited
			friendsInvited += j - currentlyStanding
			currentlyStanding += int(audience[j]) + friendsInvited
	print '***invited ', friendsInvited, 'friends****'
	 #    if j==0: #how many people aren't shy
	 #        currentlyStanding += int(audience[j])
	 #        print "Level zero, currentlyStanding = ", currentlyStanding
	 #    elif currentlyStanding >= j:
	 #    	print "blah!" #if this situation is good for people
		# 	#     print "it is enough!"
		# 	#     print "Current level = ", j
		# 	#     print "currentlyStanding = ", currentlyStanding
		# 	#     currentlyStanding += int(audience[j])
		# else:
		#  	print "blah blah!"
	 #  #       friendsInvited += j - currentlyStanding
	 #  #       currentlyStanding += int(audience[j])
        
	outputFile.write("Case #%d: %d\n" %(i+1, friendsInvited))

outputFile.close()
