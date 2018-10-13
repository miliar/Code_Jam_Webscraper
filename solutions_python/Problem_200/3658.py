input = open("B-large.in")
numberOfInputs = int(input.readline())
i = 1


def isTidy(x):
	xAsStr = str(x)
	maxDigit = -1
	for c in xAsStr:
		if int(c) < maxDigit:
			return False
		maxDigit = int(c)
	return True


def findNextSmallerTidyNumber(x):
	xAsStr = str(x)
	for j in range(0, len(xAsStr) - 1):
		if int(xAsStr[j]) > int(xAsStr[j + 1]):
			# print xAsStr[:j]
			# print str((int(xAsStr[j]) - 1 + 9) % 10).zfill(2)
			# print "9" * (len(xAsStr) - j - 1)
			xAsStr = xAsStr[:j] +  str((int(xAsStr[j]) + 9) % 10) + "9" * (len(xAsStr) - j - 1)
	return int(xAsStr)





for line in input:
	maxNumber = int(line)
	while not isTidy(maxNumber):
		maxNumber = findNextSmallerTidyNumber(maxNumber)
	print "Case #" + str(i) + ": " + str(maxNumber)
	i += 1
