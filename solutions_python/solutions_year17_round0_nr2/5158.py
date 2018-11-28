data = []

output = open('Output.txt', 'w')

with open('Small.txt') as inputfile:
    for line in inputfile:
    	data.append(int(line))

del data[0]

def findLastBase10(number):
	currentNumber = 1
	biggestBase10 = 1
	numberArray = []

	while currentNumber <= number:
		numberArray.append(currentNumber)
		currentNumber += 1

	for number in numberArray:
		stringNumber = str(number)
		currentNumberArray = []
		for char in stringNumber:
			currentNumberArray.append(int(char))

		if len(currentNumberArray) == 1:
			biggestBase10 = number
		else:
			prev = 0
			isTidy = True
			for i in currentNumberArray:
				if prev > i:
					isTidy = False
				prev = i
			if isTidy == True:
				biggestBase10 = number
					
	return biggestBase10

caseNumber = 1

for i in data:
	output.write("Case #" + str(caseNumber) + ": " + str(findLastBase10(i)))
	output.write('\n')
	caseNumber += 1