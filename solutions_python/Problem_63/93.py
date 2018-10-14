def getMinimumTestCnt(lower, upper, factor):
	if (lower*factor) >= upper:
		return 0
	a = lower
	while a < upper:
		a = a * factor
		tmp = upper // factor
		if (upper % factor) > 0:
			tmp = tmp + 1
		upper = tmp
	cnt = getMinimumTestCnt(lower, a, factor)
	return cnt + 1


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

	lower = int(line[0])
	upper = int(line[1])
	factor = int(line[2])

	res = getMinimumTestCnt(lower, upper, factor)
	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
