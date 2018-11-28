# This is used to solve the card trick in the Google Code Jam
dataInput = open('magicTrick.txt', 'r')
# First we read the number of test cases.
numTestCases = int(dataInput.readline())
for count in range(0, numTestCases):
	# now we read the data and find the results.
	# First we read the Data for the first part.
	choice1 = int(dataInput.readline())
	rowData1 = [0, 0, 0, 0]
	for i in range(0, 4):
		rowData1[i] = list(dataInput.readline().strip().split(' '))
	choice2 = int(dataInput.readline())
	rowData2 = [0, 0, 0, 0]
	for i in range(0, 4):
		rowData2[i] = list(dataInput.readline().strip().split(' '))
	# now we have to check how many of the characters match in both the rows
	matchCount = 0
	matchElement = -1
	for item in rowData1[choice1 - 1]:
		if item in rowData2[choice2 - 1]:
			matchCount = matchCount + 1
			matchElement = item
	mesg = "Case #" + str(count + 1) + ": "
	if matchCount == 1:
		# Perfect Match
		mesg = mesg + matchElement
	elif matchCount > 1:
		# Bad Magician
		mesg = mesg + "Bad magician!"
	elif matchCount == 0:
		# Cheater
		mesg = mesg + "Volunteer cheated!"
	print(mesg)