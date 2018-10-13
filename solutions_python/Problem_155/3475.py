# James Lindamood
# CodeJam Round 1 Problem 1
import sys

def findMinFriendsNeeded(argList):

	# Init Vars
	friendsNeeded = 0
	audienceStanding = 0
	shynessMax = int(argList[0])
	shynessBreakdown = str(argList[1])

	# Friends needed = sum of all friends needed to get sMax to stand
	for x in xrange(0,shynessMax + 1):
		if audienceStanding >= x:
			audienceStanding += int(shynessBreakdown[x])
		if audienceStanding < x:
			friendsNeeded += (x - audienceStanding)
			audienceStanding += (x - audienceStanding)
			audienceStanding += int(shynessBreakdown[x])
	return friendsNeeded

# Input Parse
if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		inputFile = sys.argv[1]
		if inputFile != '-':
			inputFile = open(inputFile)

	cases = inputFile.readlines();
	numberOfCases = cases.pop(0)

	outputFile = open("r1p1output.txt", "w+b")
	caseNumber = 1
	for x in xrange(0, len(cases)):
		testCase = []
		testCaseString = cases.pop(0).strip()
		testCase.append(int(testCaseString[0]))
		testCase.append(str(testCaseString[2:]))
		answer = findMinFriendsNeeded(testCase)
		print "Case #%s: %s" % (caseNumber, str(answer))
		outputFile.write("Case #%s: %s\n" % (caseNumber, str(answer)))
		caseNumber += 1
	outputFile.close()