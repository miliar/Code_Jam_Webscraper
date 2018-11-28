import cjio
import re


def biggestEmptyBlocksOfStalls(stalls):
	# print('asdf')
	match = re.finditer(r'\.+', stalls)
	matchInfo = [(i.start(), i.end()-i.start()) for i in match]
	maxLength = max([i[1] for i in matchInfo])
	largestBlocksOnly = [i[0] for i in matchInfo if i[1] == maxLength]
	# find middle ones in all of the largest blocks
	if maxLength % 2 == 0:
		even = True
	else:
		even = False

	middleIdxs = []
	for i in largestBlocksOnly:
		middleIdxs.append(i+int(maxLength/2))
		if even:
			middleIdxs.append(i+int(maxLength/2)-1)

	return middleIdxs, maxLength
print(biggestEmptyBlocksOfStalls('#......#......#'))

def createLsRsMap(stallIdxsToMap, maxLength):
	# if maxLength is even we expect all stallIdxs to be in pairs
	# as there are two middle elements in a list of even length
	if maxLength % 2 == 0:
		even = True
	else:
		even = False

	lsRsMap={}

	half = int(maxLength/2)
	if even: 
		for r, l in zip(stallIdxsToMap[::2], stallIdxsToMap[1::2]):
			assert(l == r-1)
			lsRsMap[l] = half, half-1
			lsRsMap[r] = half, half-1
	else:
		for idx in stallIdxsToMap:
			lsRsMap[idx] = half, half

	return lsRsMap
print(createLsRsMap(*biggestEmptyBlocksOfStalls('#......#......#')))


def chooseStall(lsRsMap):
	potentialIdxs = lsRsMap.keys()
	return min(potentialIdxs)
print(chooseStall(createLsRsMap(*biggestEmptyBlocksOfStalls('#......#......#'))))

def stallProblem(n, k):
	"""
		n: total number of stalls, less 2. (two guard stalls on either side)
		k: number of people who will fill empty stalls one by one.

		returns min(Ls, Rs) and max(Ls, Rs) for the last person.
	"""

	# stalls: as string. 
	# empty stall: .
	# filled stall: #

	# initial stall with guards on either end
	stalls = '#' + '.'*n + '#'
	assert len(stalls) == n + 2
	# print(stalls)

	# insert people one by one
	for i in range(k):
		# look for biggest contiguous block of empty stalls and get index/indices of all the middle
		# ones
		idxs, maxLength = biggestEmptyBlocksOfStalls(stalls)

		# then for each one compute max(Ls, Rs) and min(Ls, Rs)
		# dict that maps idx to tuple of max and min LsRs
		stallMap = createLsRsMap(idxs, maxLength)

		# choose a stall
		stallToOccupy = chooseStall(stallMap)

		# update stalls
		# assert(stalls[stallToOccupy] == '.', "can't occupy occupied stall")
		stalls = stalls[:stallToOccupy] + '#' + stalls[stallToOccupy+1:]
		# print(stalls)
	return stallMap[list(stallMap.keys())[0]]

# print(stallProblem(1000, 1))


if __name__ == '__main__':
	inputFile = r"C:\Users\ed\codejam2017\C-small-1-attempt0.in"
	outputFile = r"C:\Users\ed\codejam2017\C-small-1-attempt0.out"

	num, data = cjio.parseFile(inputFile)
	res = []
	for i in data:
		iSplit = i.split(' ')
		n = int(iSplit[0])
		k = int(iSplit[1])
		solution=stallProblem(n, k)
		res.append("{} {}".format(solution[0], solution[1]))

	cjio.generateOutput(outputFile, res, num)
