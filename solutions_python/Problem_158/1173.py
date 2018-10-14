# James Lindamood
# Codejam Round 1 Problem 2
import sys

# Logic
# X = 1, Gabriel always wins
# X = 2, Gabriel wins when grid 2x1, 2x2, 4x1, or 4x4, or 4x2
# X = 3, 
# Function

def whoWins(argList):

	x = int(argList[0])
	r = int(argList[2])
	c = int(argList[4])

	if x == 1:
		return "GABRIEL"

	if x == 2:
		if r == 2 or c == 4:
			return "GABRIEL"
		if r == 4 or c == 2:
			return "GABRIEL"
		return "RICHARD"

	if x == 3:
		if r == 2 and c == 3:
			return "GABRIEL"
		if r == 3 and c == 2:
			return "GABRIEL"
		if r == 4 and c == 3:
			return "GABRIEL"
		if r == 3 and c == 4:
			return "GABRIEL"
		if r == 3 and c == 3:
			return "GABRIEL"
		return "RICHARD"

	if x == 4:
		if r == 3 and c == 4:
			return "GABRIEL"
		if r == 4 and c == 3:
			return "GABRIEL"
		if r == 4 and c == 4:
			return "GABRIEL"
		return "RICHARD"



# Input Parse
if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		inputFile = sys.argv[1]
		if inputFile != '-':
			inputFile = open(inputFile)

	cases = inputFile.readlines();
	numberOfCases = cases.pop(0)

	outputFile = open("r1p4output.txt", "w+b")
	caseNumber = 1
	for x in xrange(0, len(cases)):
		testCase = []
		testCase.append(cases.pop(0).strip())
		answer = whoWins(testCase[0])
		print "Case #%s: %s\n" % (caseNumber, str(answer))
		outputFile.write("Case #%s: %s\r\n"  % (caseNumber, str(answer)))
		caseNumber += 1
	outputFile.close()