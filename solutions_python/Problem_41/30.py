#!/usr/bin/python

def readInput():
	file = open('B-large.in')
	testCaseCount = int(file.readline().rstrip())

	testCases = [file.readline().rstrip() for i in range(0, testCaseCount)]
	return testCases

def nextNumber(number):
	for i in range(len(number) - 2, -1, -1):
		if number[i] < number[i + 1]:
			lowest = number[i + 1]
			for j in range(i + 2, len(number)):
				if number[j] < lowest and number[j] > number[i]:
					lowest = number[j]

			digitsAfterI = [d for d in number[i+1:]]
			digitsAfterI.remove(lowest)
			digitsAfterI.append(number[i])
			digitsAfterI.sort()
			return number[:i] + lowest + ''.join(digitsAfterI)

	digits = [i for i in number]
	digits.sort()
	firstNonZeroDigit = ''.join(digits).lstrip('0')[0]
	digits.remove(firstNonZeroDigit)
	
	return firstNonZeroDigit + '0' + ''.join(digits)

testCases = readInput()
testCaseNumber = 1

for testCase in testCases:
	print "Case #%s: %s" % (testCaseNumber, nextNumber(testCase))
	testCaseNumber += 1
