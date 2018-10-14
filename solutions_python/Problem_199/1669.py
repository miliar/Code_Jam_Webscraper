import math
import functools

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
				s,k = lineString.split(' ')
				cases.append((s,int(k)))
	return numCases, cases

@functools.lru_cache(maxsize = 8192)
def solve(s, k):
	# Returns the number of flips needed to get all the pancakes happy side up, or math.inf if impossible

	pancakes = list(s)

	# truncate already flipped pancakes on each side
	numberCorrect = max(l for l in range(len(pancakes)+1) if all(c == '+' for c in pancakes[0:l]))
	pancakes = pancakes[numberCorrect:]

	pancakes = pancakes[::-1]
	numberCorrect = max(l for l in range(len(pancakes)+1) if all(c == '+' for c in pancakes[0:l]))
	pancakes = pancakes[numberCorrect:]

	# base case: no more pancakes need to be flipped
	if len(pancakes) == 0:
		return 0

	# base case: impossible
	elif len(pancakes) < k:
		return math.inf

	# try to perform one flip at each end and recursively solve
	flipsRequiredEachEnd = []
	for pancakeSide in (pancakes[:], pancakes[::-1]):
		for i in range(k):
			if pancakeSide[i] == '-':
				pancakeSide[i] = '+'
			else:
				pancakeSide[i] = '-'

		flipsRequiredEachEnd.append(solve(''.join(pancakeSide), k))

	return 1 + min(flipsRequiredEachEnd)

if __name__ == '__main__':

	# read the input
	numCases, cases = readInput('A-small-attempt0.in')

	# open output file
	with open('output.out', 'w') as outputFile:

		# solve each case
		for i, (s,k) in enumerate(cases):
			result = solve(s,k)

			# write results
			outputFile.write('Case #{0}: '.format(i+1))
			if result == math.inf:
				outputFile.write('IMPOSSIBLE')
			else:
				outputFile.write(str(result))
			outputFile.write('\n')