#!/usr/bin/python

if __name__ == "__main__":
	outputFile = open("A.out", "w") 
	data = [[int(numStr) for numStr in line.split()] for line in open("A.in", "r")]
	#print data
	numOfCase = data[0][0]
	dataIndex = 1
	for caseIndex in range(numOfCase):
		mushroomNumList = data[(caseIndex + 1) * 2]
		eatenMushroomNum1 = 0
		largestDiff = 0
		for i in range(len(mushroomNumList) - 1):
			haveToEatNum = max(mushroomNumList[i] - mushroomNumList[i + 1], 0);
			largestDiff = max(haveToEatNum, largestDiff)
			eatenMushroomNum1 += haveToEatNum
		
		eatenMushroomNum2 = 0
		for i in range(len(mushroomNumList) - 1):
			if mushroomNumList[i] <= largestDiff:
				eatenMushroomNum2 += mushroomNumList[i]
			else:
				eatenMushroomNum2 += largestDiff
				
		'''
		firstLineIndex = data[dataIndex][0]
		firstLine = data[dataIndex + firstLineIndex]
		dataIndex += 5
		secondLineIndex = data[dataIndex][0]
		secondLine = data[dataIndex + secondLineIndex]
		dataIndex += 5
		commonElement = list(set(firstLine) & set(secondLine))
		if len(commonElement) == 0:
			result = "Volunteer cheated!"
		elif len(commonElement) == 1:
			result = str(commonElement[0])
		else:
			result = "Bad magician!"
			'''
		outputLine = "Case #%d: %s %s\n" % (caseIndex + 1, eatenMushroomNum1, eatenMushroomNum2)
		outputFile.write(outputLine)
	outputFile.close()
