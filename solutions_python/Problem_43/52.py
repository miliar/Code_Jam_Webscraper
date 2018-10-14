def getMinimum(numstr):
	strlen = len(numstr)

	digitDic = {}
	digitDic[numstr[0]] = 1
	n = 2

	for i in range(1, strlen):
		ch = numstr[i]
		if ch not in digitDic:
			digitDic[ch] = n
			n += 1

	#print digitDic
	for key in digitDic.keys():
		if digitDic[key] == 2:
			digitDic[key] = 0
		elif digitDic[key] > 2:
			digitDic[key] = digitDic[key] - 1

	base = len(digitDic.keys())
	if base == 1:
		base = 2

	sum = 0
	for i in range(strlen):
		sum = sum + digitDic[numstr[strlen-1-i]]*(base**i)

	return sum


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
	numstr = lines[idx][0:-1]
	idx += 1

	res = getMinimum(numstr)
	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
