import math

def getInput(inputFileName):
	intervals = []

	with open(inputFileName, 'r') as inputFile:
		testCases = int(inputFile.readline())

		for testCaseNum in range(testCases):
			interval = inputFile.readline().strip().split(' ')
			intervals.append(interval)

	return intervals

def isPalindrome(number):
	digits = list(str(number))
	digitsReversed = list(reversed(digits))

	for (counter, digit) in enumerate(digits):
		if (digit != digitsReversed[counter]):
			break
	else:
		return True

	return False

def isSquare(number):
	square = math.sqrt(number)
	if (square > 0 and square == int(square)):
		return True, int(square)

	return False, None

def isFairAndSquare(number):
	if (isPalindrome(number)) :
		isItSquare, square = isSquare(number)

		if (isItSquare and isPalindrome(square)):
			return True

	return False

def writeOutput(outputFileName, content):
	 with open(outputFileName, 'w') as outputFile:
	 	outputFile.write(content)

#------------------------------------------------------------------------------

output = '';

intervals = getInput('input')

for (counter, interval) in enumerate(intervals):
	numberOfFairAndSquares = 0

	for number in range(int(interval[0]), int(interval[1]) + 1):
		if (isFairAndSquare(number)):
			numberOfFairAndSquares += 1

	output += "Case #{0}: {1}\n".format(counter + 1, numberOfFairAndSquares)

writeOutput('output', output)



