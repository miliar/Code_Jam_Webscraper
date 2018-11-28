inputFile = open('A-large.in', 'r')
inString = inputFile.read()
inputLines = inString.split('\n')
inputLines.pop(0)
output = ''
case = 1
i = 0
for line in inputLines:
	if i == 1:
		i -= 1
		mushroomIncrements = line.split(' ')
		mushroomIncrements = map(int, mushroomIncrements)
		methodOneMin = 0
		methodTwoMin = 0
		methodTwoMaxEat = 0
		differences = []
		for j in range(len(mushroomIncrements) - 1):
			difference = mushroomIncrements[j] - mushroomIncrements[j + 1]
			differences.append(difference)
			if mushroomIncrements[j] > mushroomIncrements[j + 1]:
				methodOneMin += difference
			if difference > methodTwoMaxEat:
				methodTwoMaxEat = difference
		if methodTwoMaxEat == -1:
			methodTwoMaxEat = 0
		j = 0 
		for difference in differences:
			methodTwoMin += min(mushroomIncrements[j], methodTwoMaxEat)
			j += 1
		output += ('Case #' + str(case) + ': ' + str(methodOneMin) + ' ' + str(methodTwoMin) + '\n')	
		case += 1
	else:
		i += 1
	
outputFile = open('out.out', 'w')
outputFile.write(output)