import math
import time

inputName = input("> ")
inputFile = open(inputName, "r")
outputFile = open("tidyNumbersOut.txt", "w")

def isTidy(num):
	numStr = str(num)
	for i in range(1, len(numStr)):
		if int(numStr[i]) < int(numStr[i - 1]):
			return False
	return True

testCases = int(inputFile.readline())
for i in range(testCases):
	testNum = int(inputFile.readline())
	j = testNum
	while j > 0:
		if isTidy(int(j)):
			if i < testCases - 1:
				outputFile.write("Case #" + str(i + 1) + ": " + str(j) + "\n")
			else:
				outputFile.write("Case #" + str(i + 1) + ": " + str(j))
			break
		else:
			testStr = str(int(j))
			for k in range(2, len(testStr)):
				if not isTidy(int(testStr[:k])):
					j -= int(testStr[k:])
					break
		j -= 1
outputFile.close()