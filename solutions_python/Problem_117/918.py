import sys


if len(sys.argv) != 2:
	sys.exit("Please specify test input file")
inputFilePath = sys.argv[1]
inputFile = open(inputFilePath, 'r')

numberOfTestCases = -1
patterns = []
pattern = None
n = -1
m = -1
counter = 0

lineNumber = 0
for line in inputFile.readlines():
	if 0 == lineNumber:
		numberOfTestCases = int(line)
	elif (n < 0 and m < 0) or counter == n:
		tmp = line.rstrip('\n').split(' ');
		n = int(tmp[0])
		m = int(tmp[1])
		counter = 0
		if None != pattern:
			patterns.append(pattern)
		pattern = []
	else:
		counter += 1
		tmp = line.rstrip('\n').split(' ')
		row = []
		for e in tmp:
			row.append(int(e))
		pattern.append(row)
	lineNumber += 1
patterns.append(pattern)

inputFile.close()

######################################

def checkPattern(pattern):
	n = len(pattern)
	m = len(pattern[0])

	drows = []
	dcols = []

	for i in range(0, n):
		mr = max(pattern[i])
		drows.append([mr] * m)

	for j in range(0, m):
		mr = 0
		for i  in range(0, n):
			mr = max(pattern[i][j], mr)
		dcols.append([mr] * n)

	restored = []
	for i in range(0, n):
		row = []
		for j in range(0, m):
			a = drows[i][j]
			b = dcols[j][i]
			row.append(min(a, b))
		restored.append(row)

	return pattern == restored


#####################################
counter = 0
for pattern in patterns:
	counter += 1
	#print checkPattern(pattern)
	if checkPattern(pattern):
		print "Case #" + str(counter) + ": YES"
	else:
		print "Case #" + str(counter) + ": NO"
