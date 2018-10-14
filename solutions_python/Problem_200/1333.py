import re
import sys

numbers = []
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
			numbers.append(int(line.strip()))

		lineNumb = lineNumb + 1

def solve(number):
	# strNum = str(number)

	# lastDigit = strNum[-1]
	lastDigit = number % 10

	solution = number;


	while(int("".join(sorted(str(solution)))) != solution):
		strNumber = str(solution)
		for d in range(len(strNumber) - 1):
			digit0 = int(strNumber[d]);
			digit1 = int(strNumber[d+1]);
			if digit0 > digit1:
				strNumber = list(strNumber)
				strNumber[d] = str(int(strNumber[d]) - 1);
				for d2 in range(d+1, len(strNumber)):
					strNumber[d2] = '9'

		newSolution = int("".join(strNumber))

		if newSolution == solution:
			solution = -1
			break;

		solution = newSolution

	return solution


solution = []

for n in numbers:
	solution.append(solve(n));

outputSolution(solution)