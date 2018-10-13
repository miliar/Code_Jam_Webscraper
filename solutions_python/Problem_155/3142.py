###### Google Code Jam Qualification Round: A. Standing Ovation

inputfile = open('A-large.in')
outputfile = open('output.txt', 'w')
shynessData = []
numCases = int(inputfile.readline())


### Build the data list
for line in inputfile:
	currentLine = line.strip().split(' ')
	shynessData.append([int(currentLine[0]), currentLine[1]])


### Determine solution
# loop through each test case
for testNum, case in enumerate(shynessData):
	numStanders = 0
	numFriends = 0
	
	# loop through the string encoding number of audience members at each shyness level
	for i, c in enumerate(case[1]):
		# the number of audience members at shyness level i
		numAudience = int(c)

		if (i == 0):
		# add the level 0 shyness level first
			numStanders += numAudience
		elif (numAudience > 0):
		# only check the next shyness levels if they're not empty
			if (numStanders + numFriends >= i):
			# check if there are enough standers for the current shyness level
				numStanders += numAudience
			else:
			# if not, add min number of friends
				numFriends += (i - (numStanders + numFriends))
				numStanders += numAudience

	outputfile.write("Case #" + str(testNum + 1) + ": " + str(numFriends) + "\n")



