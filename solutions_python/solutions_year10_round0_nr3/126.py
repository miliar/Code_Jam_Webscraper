def getTotalPeoples(runCnt, seatCnt, groups):
	groupCnt = len(groups)
	groupIdx = 0
	prevPeople = [-1] * groupCnt
	prevRun = [-1] * groupCnt
	totalPeople = 0

	if seatCnt >= sum(groups):
		return runCnt * sum(groups)

	r = 0
	while r < runCnt:
		if prevPeople[groupIdx] != -1:
			repeatPeople = totalPeople - prevPeople[groupIdx]
			repeatRun = r - prevRun[groupIdx]
			repeatCnt = (runCnt - r) // repeatRun
			totalPeople = totalPeople + (repeatCnt*repeatPeople)
			r = r + (repeatCnt*repeatRun)

			while r < runCnt:
				restSeat = seatCnt
				while restSeat >= groups[0]:
					restSeat = restSeat - groups[0]
					totalPeople = totalPeople + groups[0]
					groups.append(groups[0])
					del groups[0]
				r = r + 1

			return totalPeople

		else:
			prevPeople[groupIdx] = totalPeople
			prevRun[groupIdx] = r
			restSeat = seatCnt
			while restSeat >= groups[0]:
				restSeat = restSeat - groups[0]
				totalPeople= totalPeople + groups[0]
				groupIdx = (groupIdx + 1) % groupCnt
				groups.append(groups[0])
				del groups[0]
			r = r + 1
	return totalPeople


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

	runCnt = int(line[0])
	seatCnt = int(line[1])
	groupCnt = int(line[2])

	line = lines[idx].split(' ')
	idx += 1

	groups = []
	for numberStr in line:
		groups.append(int(numberStr))

	res = getTotalPeoples(runCnt, seatCnt, groups)
	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
