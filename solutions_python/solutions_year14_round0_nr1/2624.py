import string, sys

sourceName = sys.argv[1]
outputName = sys.argv[2]
source = open(sourceName)
output = open(outputName, 'w')

def solve(case, firstNumber, firstMatrix, secondNumber, secondMatrix):
	result = ""
	candidate = set(firstMatrix[firstNumber-1]).intersection(set(secondMatrix[secondNumber-1]))
	if len(candidate) == 1:
		result = "Case #%d: %d" % (case+1, list(candidate)[0])
	elif len(candidate) > 1:
		result = "Case #%d: Bad magician!" % (case+1)
	else:
		result = "Case #%d: Volunteer cheated!" % (case+1)
	print result
	output.write(result + "\n")

testcase = int(source.readline())
for i in range(testcase):
	firstNumber = int(source.readline())
	firstMatrix = []
	for j in range(4):
		firstMatrix.append([int(n) for n in source.readline().split()])
	secondNumber = int(source.readline())
	secondMatrix = []
	for j in range(4):
		secondMatrix.append([int(n) for n in source.readline().split()])
	solve(i, firstNumber, firstMatrix, secondNumber, secondMatrix)