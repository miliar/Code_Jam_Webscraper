from sets import Set
 
def handleTestCase(inputLines, testCaseNumber) :
	firstRowIndex = int(inputLines[0]) - 1 
	secondRowIndex = int(inputLines[5]) - 1
	repartition = inputLines[1:5]
	firstRow = Set(repartition[firstRowIndex].split(" "))
	repartition = inputLines[6:10]
	secondRow = Set(repartition[secondRowIndex].split(" "))
	intersection = firstRow.intersection(secondRow)
	intersection = list(intersection)
	if len(intersection) == 1 :
		return "Case #{0}: {1}".format(testCaseNumber, intersection[0])
	if len(intersection) == 0 :
		return "Case #{0}: {1}".format(testCaseNumber, "Volunteer cheated!")
	if len(intersection) > 1 :
		return "Case #{0}: {1}".format(testCaseNumber, "Bad magician!")




f = open("A-small-attempt0.in")
lines = map(lambda x : x.strip("\n"),f.readlines())
outputlines = []

# parse input
testCases = int(lines[0])
for i in range(testCases) :
	testCase = lines[(i * 10 + 1): (i*10 + 11)]
	outputlines.append(handleTestCase(testCase, i + 1))  
print outputlines

outputfile = open("output.txt","w")
outputfile.writelines(map(lambda x : x + "\n", outputlines))