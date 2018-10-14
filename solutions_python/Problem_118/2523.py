def inFile(path):
	fileHandle = open(path)
	fileList = fileHandle.readlines()
	fileHandle.close()
	
	DataSet = []

	TestCases = dataHandle(fileList)
	numTest = int(TestCases.pop())
	for i in range(0,numTest):
		case = TestCases.pop().split()
		lower = int(case[0])
		upper = int(case[1])
		DataSet.append((lower,upper))
	
	return DataSet, numTest

def dataHandle(rawdata):
	TestCases = []
	for d in rawdata:
		temp = d.strip('\n')
		TestCases.append(temp)
	TestCases.reverse()

	return TestCases

def outFile(path, resultset):
	fileHandle = open(path, 'w+')
	num = 1
	for i in range(0,len(resultset)):
		t = 'Case #' + str(num) + ': ' + str(resultset[i]) + '\n'
		fileHandle.writelines(t)
		num += 1
	fileHandle.close

def palindromeSet(data):
	results = []
	for i in range(data[0],data[1]+1):
		if Ispalindrome(i):
			results.append(i)
	return results

def Ispalindrome(number):
	strlist = list(str(number))
	temp = list(str(number))
	temp.reverse()
	if strlist == temp:
		return True


def square(data):
	results = []
	for i in range(data[0],data[1]+1):
		for x in range (1,i+1):
			if x*x == i and Ispalindrome(x):
				results.append(i)
	return results

def fair(dataset, numtest):
	results = []
	details = []
	for i in range(0,numtest):
		number = 0
		detail = []
		data = dataset[i]
		palset = palindromeSet(data)
		sqrset = square(data)
		print "p:" ,palset
		print "s:" ,sqrset

		for s in sqrset:
			if s in palset:
				number += 1
				detail.append(s)
		results.append(number)
		details.append(detail)
	print details
	return results




if __name__ == '__main__':
	inpath = '/Users/inzen/in'
	outpath = '/Users/inzen/out'
	
	dataset, numtest = inFile(inpath)
	print dataset, numtest
	
	results = fair(dataset, numtest)

	outFile(outpath, results)
