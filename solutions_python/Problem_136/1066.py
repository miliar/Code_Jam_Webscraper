from multiprocessing import *

Cs = 2.0

def evaluateResults(testCaseNumber):
	testCase = dataset[testCaseNumber].split()
	C = float(testCase[0])
	F = float(testCase[1])
	X = float(testCase[2])
	i = 0
	results = []
	temp = 0
	while True:#i < (X/C):
		results.append( ( X/(Cs+(i*F)) ) + temp)
		temp += (C/(Cs + (i*F)))
		i += 1
		if ( results[-1] > min(results)):
			break;
	print "Case #" + str(testCaseNumber+1) + ": " + str(min(results))
	return testCaseNumber, "Case #" + str(testCaseNumber+1) + ": " + str(min(results))
		
#Initialise the execution of x parallel threads so to run the test for different values of k concurrently
def initialiseSystem(tests):
	po = Pool(processes=(cpu_count()-1 if cpu_count() > 2 else 2))
	res = po.map_async(evaluateResults,((k) for k in tests))
	results = res.get()
	
	return list(results)
	
def cookieClicker():
	global dataset
	dataset = loadFile('B-large.in')
	dataset = dataset.splitlines()
	testCases = int(dataset[0])
	dataset = dataset[1:]
	results = initialiseSystem(range(0,testCases))
	results.sort()
	file = open("B-large.out", "w")
	for x,y in results:
		file.write(y + "\n")
	pass
	file.close()
	
def loadFile(filePath):
	file = open(filePath)
	fileData = file.read()
	file.close()
	return fileData

	pass	
	
def writeToFile(output):
	file.write(output + "\n")

if __name__ == "__main__":
	cookieClicker()