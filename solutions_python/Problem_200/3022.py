from math import pow

def toNine(upperBound, number, index):
	numList = [int(d) for d in str(number)]
	nextStep = 1

	# Find positive step
	tens = int(pow(10, (len(numList) - index - 1)))
	nextStep = (9 - numList[index]) * tens

	# Find negative step if positive step isn't usable
	if (number + nextStep) > upperBound:
		# Find negative step
		if index != (len(numList) - 1):
			tens = int(pow(10, (len(numList) - index - 2)))
			nextStep = -((numList[index + 1] + 1) * tens)
		else:
			tens = int(pow(10, (len(numList) - index - 1)))
			nextStep = -((numList[index] + 1) * tens)

	return nextStep

def isTidy(upperBound, number):
	numList = [int(d) for d in str(number)]
	tidy = True
	nextStep = 1

	for i in range(0, len(numList) - 1):
		thisDigit = numList[i]
		for k in range(i + 1, len(numList)):
			compareDigit = numList[k]
			if thisDigit > compareDigit:
				nextStep = toNine(upperBound, number, k)
				tidy = False
				break
		if tidy == False:
			break
	return { 'tidy': tidy, 'nextStep': nextStep }

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(0, t):
	endCount = int(input())
	tempCount = endCount

	while tempCount > 10:
		tidyCheck = isTidy(endCount, tempCount)
		if tidyCheck['tidy']:
			lastTidy = tempCount
			break
		else:
			tempCount += tidyCheck['nextStep']
	print("Case #{}: {}".format(i + 1, tempCount))
	# check out .format's specification for more formatting options