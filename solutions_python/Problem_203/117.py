def allblank(string):
	for char in string:
		if char !='?':
			return False
	return True

def rectanglify(string):
	input = list(string)
	firstchar = ''
	lastchar = ''
	for k in range(len(input)):
		if input[k] == '?' and lastchar != '':
			input[k] = lastchar
		elif input[k] != '?':
			lastchar = input[k]
			if firstchar == '':
				firstchar = input[k]
	for k in range(len(input)):
		if input[k] != '?':
			return ''.join(input)
		input[k] = firstchar
		
def fullrectanglify(listofstrings):
	input = listofstrings[:]
	firstrow = ''
	lastrow = ''
	for k in range(len(input)):
		if allblank(input[k]) and lastrow != '':
			input[k] = lastrow
		elif not allblank(input[k]):
			input[k] = rectanglify(input[k])
			lastrow = input[k]
			if firstrow == '':
				firstrow = input[k]
	for k in range(len(input)):
		if not allblank(input[k]):
			return input
		input[k] = firstrow

import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		firstInput = [int(x) for x in inputLines.pop(0).rstrip().split()]
		listOfStrings = []
		for k in range(firstInput[0]):
			listOfStrings.append(inputLines.pop(0).rstrip())
		output = fullrectanglify(listOfStrings)
		fileOUT.write('Case #' + str(num+1) + ': ' + '\n')
		for item in output:
			fileOUT.write(item + '\n')