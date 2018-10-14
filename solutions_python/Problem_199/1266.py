import re
import sys
import math

cases = list()
lineNumb = 0;
testCases = 0;

def outputSolution(solution):
	countSolution = 1;

	for s in solution:
		print "Case #"+str(countSolution)+": "+str(s);
		countSolution = countSolution + 1


with open(sys.argv[1]) as file:
	for line in file:

		if(lineNumb == 0):
			testCases = int(line.strip())
		
		else:
			data = line.strip().split(" ")
			test = dict()
			test["S"] = list(data[0])
			test["K"] = int(data[1])
			cases.append(test)

		lineNumb = lineNumb + 1

def check(status):
	for s in status:
		if s!= '+':
			return False

	return True

def flip(status, position, K):
	length = len(status)
	# print status
	# print K
	# print position
	if length - position >= K:
		for p in range(position, position + K):
			if status[p] == "+":
				status[p] = "-"
			else:
				status[p] = "+"

	return status

def solve(case):
	moveCount = 0;

	pancackes = case['S']
	flipper = case['K']

	# print pancackes
	# print flipper

	attemps = list()
	attemps.append( "".join(pancackes) )

	while(check(pancackes) == False):
		newStatus = list(pancackes)
		for p in range(len(pancackes)):
			if pancackes[p] == "-":
				newStatus = flip(newStatus, p, flipper);
				break;

		if "".join(newStatus) in attemps:
			return "IMPOSSIBLE"
		else:
			pancackes = list(newStatus)
			moveCount = moveCount+1;
			attemps.append("".join(pancackes))

	return moveCount;


solution = []

# print cases

for c in cases:
	solution.append(solve(c));

outputSolution(solution)