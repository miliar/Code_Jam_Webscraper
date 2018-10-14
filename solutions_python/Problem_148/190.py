# in: filename
# out: list - index i in list -> line i+1 of file (trimmed)

def readFile(filename):
	f = open(filename,'r')
	file = f.readlines()
	f.close()
	trimmedFile = [x.strip() for x in file]
	return trimmedFile
	
# in: filename
# out: list - index i in list -> case i+1 in file as list' such that index j in list' -> line j+1 in case 
	
def divideIntoTests(filename,linesPerTest):
	data = readFile(filename)
	numTestCases = int(data[0])
	testCases = [data[x*linesPerTest+1:(x+1)*linesPerTest+1] for x in xrange(0,numTestCases)]
	return testCases
	
def stringToNumbers(iter):
	return map(int,iter.split())
	
def testsAsNumbers(filename,linesPerTest):
	testCases = divideIntoTests(filename,linesPerTest)
	numberTests = []
	for testCase in testCases:
		numberTests.append([map(int,s.split()) for s in testCase])
	return numberTests

def solveOne(fileList, capacity):
	counter = 0
	fileList.sort()
	while fileList:
		firstFile = fileList[len(fileList)-1]
		secondFile = 1
		if len(fileList) == 1:
			counter += 1
			return counter
		while ((secondFile < len(fileList)) and (firstFile + fileList[secondFile] <= capacity)):
			secondFile += 1
		if ((firstFile + fileList[secondFile-1] <= capacity)):
			fileList.pop(secondFile-1)
		if (len(fileList)):
			fileList.pop(len(fileList)-1)
		counter += 1
	return counter
	
def solveAll(filename):
	f = open(filename + " output","w")
	data = testsAsNumbers(filename,2)
	for i in range(len(data)):
		f.write("Case #%d: %d\n" % (i+1,solveOne(data[i][1],data[i][0][1])))
	f.close()