def get1s(cnt):
	return (1 << cnt) - 1


def getBulbStatus(snapperCnt, snapCnt):
	allSnapperON = get1s(snapperCnt)
	if (snapCnt & allSnapperON) == allSnapperON:
		return "ON"
	else:
		return "OFF"


import sys
#import pdb

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

#pdb.set_trace()
for test in range(testcnt):
	line = lines[idx].split(' ')
	idx += 1
	snapperCnt = int(line[0])
	snapCnt = int(line[1])

	res = getBulbStatus(snapperCnt, snapCnt)
	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
