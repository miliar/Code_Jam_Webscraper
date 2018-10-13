#Google Code Jam: Qualification Round - A. Magic Trick

inputfile = open('A-small-attempt0.in')
outputfile = open('output.txt', 'w')
currentRow = []
cardData = []
caseIndex = 0
caseNum = 1
numCases = int(inputfile.readline())

#Build the data list
for line in inputfile:
	currentLine = line.strip().split(' ')
	if len(currentLine) == 1:
		cardData.append(int(currentLine[0]))
	else:
		for num in currentLine:
			currentRow.append(int(num))
		cardData.append(currentRow)
		currentRow = []

#Determine Possible Solution
while caseIndex < 10*numCases:
	row1 = cardData[caseIndex]
	row2 = cardData[caseIndex + 5]
	possibleSol = list(set(cardData[caseIndex + row1]) & set(cardData[caseIndex + 5 + row2]))
	if not possibleSol:
		outputfile.write('Case #' + str(caseNum) + ': ' + 'Volunteer cheated!' + '\n')
	elif len(possibleSol) == 1:
		outputfile.write('Case #' + str(caseNum) + ': ' + str(possibleSol[0]) + '\n')
	else:
		outputfile.write('Case #' + str(caseNum) + ': ' + 'Bad magician!' + '\n')
	caseIndex += 10
	caseNum += 1