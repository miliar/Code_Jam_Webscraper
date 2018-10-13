#!/usr/bin/python -tt
import sys
import math

#Parse datas
def parseInput(fileName):
	f = open(fileName, 'rU')
	contentFile = f.readlines()
	f.close()
	
	nbCase = int(contentFile.pop(0))
	
	testCaseList = [nbCase]
	
	for i in range(nbCase):
		minMax = contentFile.pop(0).replace('\n', '').split(' ')
		testCaseList.append(minMax)

	return testCaseList

def isPalindrome(value):
	strValue = str(value)
	return strValue==strValue[::-1]

def isFairAndQSquare(value):
	squareValue = value**2
	return isPalindrome(value) and isPalindrome(squareValue)
	
def countFairAndSquare(strMin, strMax):
	minRoot = int(math.ceil(math.sqrt(int(strMin))))
	maxRoot = int(math.floor(math.sqrt(int(strMax))))

	result = 0
	for i in range(minRoot, maxRoot + 1, 1):
		if isFairAndQSquare(i):
			result+=1
	return result
	
def testAllCases(testCaseList) :
	results = []
	for i in range(int(testCaseList.pop(0))):
		results.append(countFairAndSquare(testCaseList[i][0],testCaseList[i][1]))

	return results

# Generate output file
def generateOutputFile(fileName, results):
	f = open(fileName, 'w')
	i= 1
	for result in results:
		f.write('Case #' + str(i) + ': ' + str(result) + '\n')
		i+=1
	f.close()
		
	
# Define a main() function
def main() :
	args = sys.argv[1:]
	
	if (len(args) != 2) :
		print 'usage: <sourceFile> <outputFile>'
		sys.exit(1)

	testCaseList = parseInput(args[0])
	results = testAllCases(testCaseList)
	generateOutputFile(args[1], results)

# Standard boilerplate calling main
if __name__ == '__main__':
  main()
