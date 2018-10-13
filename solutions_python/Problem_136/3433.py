Cs = 2.0

def cookieClicker():
	dataset = loadFile('B-small-attempt0.in')
	dataset = dataset.splitlines()
	testCases = int(dataset[0])
	dataset = dataset[1:]
	for testCaseNumber in range(0,testCases):
		testCase = dataset[testCaseNumber].split()
		C = float(testCase[0])
		F = float(testCase[1])
		X = float(testCase[2])
		i = 0
		results = []
		temp = 0
		while True:
			results.append( ( X/(Cs+(i*F)) ) + temp)
			temp += (C/(Cs + (i*F)))
			i += 1
			if ( results[-1] > min(results)):
				break;

		print "Case #" + str(testCaseNumber+1) + ":", min(results)
	pass
	
def loadFile(filePath):
	file = open(filePath)
	fileData = file.read()
	file.close()
	return fileData

	pass
	

if __name__ == "__main__":
	cookieClicker()