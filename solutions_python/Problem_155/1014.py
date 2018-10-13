inputFile = open('A-large.in', 'r')
inString = inputFile.read()
inputLines = inString.split('\n')
inputLines.pop(0)
output = ''
case = 1
for line in inputLines:
	relevantLine = line.split(' ')[1]
	requiredAdditions = 0
	currentOvation = 0
	currentShyness = 0
	for audienceGroupCount in list(relevantLine):
		if (int(audienceGroupCount)):	
			newAdditions = max(0, currentShyness - currentOvation)
			currentOvation += (newAdditions + int(audienceGroupCount))
			requiredAdditions += newAdditions
		currentShyness += 1
	output += ('Case #' + str(case) + ': ' + str(requiredAdditions) + '\n')	
	case += 1
outputFile = open('out5.out', 'w')
outputFile.write(output)