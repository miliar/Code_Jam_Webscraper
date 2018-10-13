import string

def getBlueMove(blueCurrPos, blueDest):
	if blueCurrPos < blueDest: return 1
	if blueCurrPos > blueDest: return -1
	if blueCurrPos == blueDest: return 0

def getOrangeMove(orangeCurrPos, orangeDest):
	if orangeCurrPos < orangeDest: return 1
	if orangeCurrPos > orangeDest: return -1
	if orangeCurrPos == orangeDest: return 0

def findMinimumTime(turns, blueButtons, orangeButtons):
	blueCurrPos = 1
	orangeCurrPos = 1
	ib = 0
	io = 0
	numberOfSeconds = 0
	for turnOf in turns:
		while (True):
			if io == len(orangeButtons): io -= 1
			if ib == len(blueButtons): ib -= 1
			blueDest = blueButtons[ib]
			orangeDest = orangeButtons[io]
			blueMove = getBlueMove(blueCurrPos, blueDest)
			orangeMove = getOrangeMove(orangeCurrPos, orangeDest)
			blueCurrPos += blueMove
			orangeCurrPos += orangeMove
			numberOfSeconds += 1
			if blueCurrPos == blueDest and blueMove == 0 and turnOf == 'B':
				ib += 1
				break
			if orangeCurrPos == orangeDest and orangeMove == 0 and turnOf == 'O':
				io += 1
				break
	return numberOfSeconds

def formTestCase(line):
	lineList = string.split(line, ' ')
	numberOfTurns = int(lineList[0])
	i = 1
	blueButtons = []
	orangeButtons = []
	turnOf = []
	while i < 2*numberOfTurns:
		turnOf += [lineList[i]]
		if lineList[i] == 'O': orangeButtons += [int(lineList[i+1])]
		if lineList[i] == 'B': blueButtons += [int(lineList[i+1])]
		i += 2
	if len(orangeButtons) == 0: orangeButtons += [-9999999]
	if len(blueButtons) == 0: blueButtons += [-9999999]
	return turnOf, blueButtons, orangeButtons
	
def openFile():
	inputFile = open('A-large.in.txt','r')
	input = inputFile.read()
	inputFile.close()
	inputLines = string.split(input,'\n')
	output = ''
	numberOfTestCases = int(inputLines[0])
	for i in range (1, len(inputLines) - 1):
		turns, blueButtons, orangeButtons = formTestCase(inputLines[i])
		print turns, blueButtons, orangeButtons
		numberOfSeconds = findMinimumTime(turns, blueButtons, orangeButtons)
		output += 'Case #%d: %d\n' % (i, numberOfSeconds)
	print output
	outputFile = open('output.txt', 'a')
	outputFile.write(output)
	outputFile.close()
	
openFile()
		