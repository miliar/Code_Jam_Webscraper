'''
Created on May 7, 2011

@author: Nathan V-C
'''

def parseListLine(testLine):
	test = testLine.strip().split(' ')
	
	i = 0
	numCombos = int(test[i])
	combos = {}
	
	for comboNum in range(i + 1, i + numCombos + 1):
		comboStr = test[comboNum]
		combo = tuple(comboStr[:2])
		
		combos[combo] = comboStr[2]
		combos[(combo[1], combo[0])] = comboStr[2]
	
	
	i += numCombos + 1
	numOpposed = int(test[i])
	opposed = {}
	
	for opposedNum in range(i + 1, i + numOpposed + 1):
		opposedStr = test[opposedNum]
		opposed0 = opposedStr[0]
		opposed1 = opposedStr[1]
		
		opposed[opposed0] = opposed1
		opposed[opposed1] = opposed0
	
	
	i += numOpposed + 1
	numElements = int(test[i])
	elements = list(test[i + 1])
	
	return combos, opposed, elements

def getFinalList(base, combos, opposed, elements):
	finalList = []
	
	for element in elements:
		listLen = len(finalList)
		# check for a combo
		if listLen > 0:
			lastElement = finalList[listLen - 1]
			try:
				element = combos[(lastElement, element)]
				finalList[listLen - 1] = element
				continue
			except KeyError:
				pass
		
		# check for opposed
		try:
			if opposed[element] in finalList:
				finalList = []
				continue
		except KeyError:
			pass
		
		finalList.append(element)
	
	return finalList

def createOutStr(listNum, numSteps):
	chars = ['[']
	for step in numSteps:
		chars.append(step + ', ')
	chars[len(chars) - 1] = chars[len(chars) - 1].replace(', ', '')
	chars.append(']')
	return 'Case #%i: %s' % (listNum, ''.join(chars))

def main(fileNameIn, fileNameOut):
	fIn = open(fileNameIn)
	fOut = open(fileNameOut, 'w')
	numLists = int(fIn.readline())
	
	base = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
	
	for listNum in range(1, numLists + 1):
		combos, opposed, elements = parseListLine(fIn.readline())
		numSteps = getFinalList(base, combos, opposed, elements)
		
		outStr = createOutStr(listNum, numSteps)
		print outStr
		fOut.write(outStr + '\n')

main('B-small-attempt1.in', 'out')