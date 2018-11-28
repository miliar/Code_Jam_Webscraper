#!/usr/bin/python

if __name__ == '__main__':
	outputFile = open("A.out", "w") 
	data = [[int(numStr) for numStr in line.split()] for line in open("A.in", "r")]
	#print data
	numOfCase = data[0][0]
	dataIndex = 1
	for caseIndex in range(numOfCase):
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
		outputLine = "Case #%d: %s\n" % (caseIndex + 1, result)
		outputFile.write(outputLine)
		'''
		audianceNumArray = []
		audianceNumArrayFormNum = data[caseIndex + 1][1]
		audianceNumArrayLength = data[caseIndex + 1][0] + 1

		for i in range(audianceNumArrayLength):
			audianceNumArray.append(audianceNumArrayFormNum % 10)
			audianceNumArrayFormNum /= 10
		
		extraAudianceNum = 0
		totalAudianceToNow = 0
		numberOfAudianceToNowLowerBound = 0
		for i in range(audianceNumArrayLength):
			#print audianceNumArray[audianceNumArrayLength - 1 - i]
			if audianceNumArray[audianceNumArrayLength - 1 - i] != 0:
				if totalAudianceToNow >= i:
					totalAudianceToNow += audianceNumArray[audianceNumArrayLength - 1 - i]
				else:
					extraAudianceNum += (i - totalAudianceToNow)
					totalAudianceToNow = i + audianceNumArray[audianceNumArrayLength - 1 - i]

		result = extraAudianceNum

		outputLine = "Case #%d: %s\n" % (caseIndex + 1, result)
		outputFile.write(outputLine)
	outputFile.close()

