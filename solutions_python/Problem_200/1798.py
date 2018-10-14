def readInput(filename):
	# reads the input and returns the number of cases and a list of (s,k) tuples
	with open(filename) as file:
		firstLineRead = False
		numCases = 0
		cases = []
		for line in file:
			lineString = line.rstrip()
			if not firstLineRead:
				numCases = int(lineString)
				firstLineRead = True
			else:
				cases.append(int(lineString))
	return numCases, cases

def isTidy(n):
	# returns whether n is tidy
	nString = str(n)

	if len(nString) == 1:
		return True

	if all(int(nString[i]) <= int(nString[i+1]) for i in range(len(nString)-1)):
		return True
	else:
		return False

def solve(n):
	# base case: n is already tidy
	if isTidy(n):
		return n

	# iteratively try to reduce each digit in the solution, maximizing the digit in the next place, until the number is tidy
	solution = n
	i = 1
	while not isTidy(solution):
		solution -= 10**i
		solution = ['0'] + list(str(solution))  # add a pad 0 in case we drop to a lower power
		solution[-i] = '9'
		solution = int(''.join(solution))
		i += 1

	return solution

if __name__ == '__main__':

	# read the input
	numCases, cases = readInput('B-large.in')

	# open output file
	with open('output.out', 'w') as outputFile:

		# solve each case
		for i, n in enumerate(cases):
			result = solve(n)

			# write results
			outputFile.write('Case #{0}: {1}\n'.format(i+1, result))
