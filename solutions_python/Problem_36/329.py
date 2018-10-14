import sys

def next(idxs, lens, n):
	while n >= 0:
		idxs[n] += 1
		if idxs[n] < lens[n]:
			for j in range(n+1, len(lens)):
				idxs[j] = 0
			return True
		else:
			n = n - 1

	return False


def countOccur(letters, target):
	strlen = len(target)
	lens = []
	for i in range(strlen):
		lens.append( len(letters[i]) )

	idxs = []
	for i in range(strlen):
		idxs.append(0)

	idx = 0
	cnt = 0
	strrange = range(strlen - 1)
	while True:
		skip = False
		terminate = False
		for i in strrange:
			if (letters[i][ idxs[i] ] >= letters[i+1][ idxs[i+1] ]):
				skip = True
				if not next(idxs, lens, i+1):
					terminate = True
					break

		if terminate:
			break
		if not skip:
			cnt += 1
			cnt = cnt % 10000
			if cnt == 0:
				print "." ,
			if not next(idxs, lens, strlen - 1):
				break
	
	print ""
	cntstr = str(cnt)
	cntstr = (4 - len(cntstr)) * '0' + cntstr
	return cntstr



fileNameIn = sys.argv[1]
#print fileNameIn[-3:]
if fileNameIn[-3:] != ".in":
	sys.exit()
fileNameOut = fileNameIn[0:-3] + ".out"
#print fileNameOut

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()
fileIn.close()


idx = 0

testCnt = int(lines[idx])	# new line?
#print "testCnt == ", testCnt
idx += 1


fileOut = open(fileNameOut, 'w')
target = "welcome to code jam"

for test in range(testCnt):

	string = lines[idx]
	idx += 1

	allLetters = {}
	for i in range(len(string)):
		if string[i] not in allLetters:
			allLetters[ string[i] ] = []
		allLetters[ string[i] ].append(i)

	fail = False
	letters = []
	for i in range(len(target)):
		if target[i] in allLetters:
			letters.append( allLetters[ target[i] ] )
		else:
			fail = True
			break

	#print str(letters)
	if fail:
		fileOut.write("Case #{0}: 0000\n".format(test+1))
		continue

	fileOut.write("Case #{0}: {1}\n".format(test+1, countOccur(letters, target)))
