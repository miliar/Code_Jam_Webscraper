def magicTrick():
	dataset = loadFile('A-small-attempt0.in')
	dataset = dataset.splitlines()
	testCases = int(dataset[0])
	dataset = list(chunks(dataset[1:], 5))
	for testCase in range(0,testCases):
		case1 = dataset[testCase*2]
		case2 = dataset[(testCase*2)+1]
		overlap = set(case1[int(case1[0])].split()).intersection( set(case2[int(case2[0])].split()) )
		result = ""
		if (len(overlap) == 1):
			result = list(overlap)[0]
		elif (len(overlap) > 1):
			result = "Bad magician!"
		else:
			result = "Volunteer cheated!"
		
		print "Case #" + str(testCase+1) + ":", result
	pass

def loadFile(filePath):
	file = open(filePath)
	fileData = file.read()
	file.close()
	return fileData

	pass
	
def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i+n]
	
	pass
if __name__ == "__main__":
	magicTrick()