def testCase (c, f, x):
	
	def segment (what, n):
		return what / (2 + n * f)
	
	n = 0
	elapsed = 0
	oldResult = None
	while True:
		newResult = elapsed + segment(x, n)
		if oldResult and oldResult < newResult:
			return oldResult
		oldResult = newResult
		elapsed += segment(c, n)
		n += 1

inputFile = open('B-small-attempt0.in', 'r')
outputFile = open('B-small-attempt0.out', 'w')

lines = [l for l in inputFile]
testsNo = int(lines[0])
for i in range(testsNo):
	caseVars = lines[i + 1].strip().split(" ")
	result = testCase(float(caseVars[0]), float(caseVars[1]), float(caseVars[2]))
	outputFile.write("Case #"+str(i + 1)+": "+str(round(result, 7))+"\n")
