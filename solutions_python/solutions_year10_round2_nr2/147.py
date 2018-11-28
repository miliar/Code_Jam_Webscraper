def getMinimumSwaps(chickCnt, targetCnt, barn, time, positions, velocities):
	positions.reverse()
	velocities.reverse()

	potentials = []
	for i in range(chickCnt):
		potentials.append(positions[i] + velocities[i]*time)

	swapTotalCnt = 0

	for i in range(targetCnt):
		if potentials[i] < barnPos:
			swapCnt = swapIntoBarn(i, barn, potentials)
			if swapCnt < 0:
				return "IMPOSSIBLE"
			else:
				swapTotalCnt = swapTotalCnt + swapCnt
	return swapTotalCnt


def swapIntoBarn(nth, barnPos, potentials):
	swapCnt = -1
	chickCnt = len(potentials)
	for i in range(nth+1, chickCnt):
		if potentials[i] >= barnPos:
			swapCnt = i - nth
			break
	if swapCnt != -1:
		while i > nth:
			tmp = potentials[i]
			potentials[i] = potentials[i-1]
			potentials[i-1] = tmp
			i = i - 1
	return swapCnt


import sys

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

for test in range(testcnt):
	line = lines[idx].split(' ')
	idx += 1

	chickCnt = int(line[0])
	targetCnt = int(line[1])
	barnPos = int(line[2])
	time = int(line[3])

	positions = []
	velocities = []

	line = lines[idx].split(' ')
	idx += 1
	for numberStr in line:
		positions.append(int(numberStr))

	line = lines[idx].split(' ')
	idx += 1
	for numberStr in line:
		velocities.append(int(numberStr))

	res = getMinimumSwaps(chickCnt, targetCnt, barnPos, time, positions, velocities)
	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
