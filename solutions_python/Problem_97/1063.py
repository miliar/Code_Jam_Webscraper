import sys

def rotate (n, digits):
	numDigits = len(str(n))
	oldStr = str(n)
	if numDigits < digits:
		oldStr = "0" + oldStr
	newStr = oldStr[-1] + oldStr[0:-1]
	return int(newStr)

numCases = int(sys.stdin.readline())
for case in xrange(1,numCases+1,1):
	sys.stdout.write ("Case #%d: " % case)
	line = sys.stdin.readline()
	numbers  = line.split(' ')
	lower = int(numbers[0])
	upper = int(numbers[1])
	
	numPairs = 0
	for currentNum in xrange(lower, upper+1, 1):
		numRotations = len(str(currentNum)) - 1
		numDigits = len(str(currentNum))
		originalNum = currentNum
		for rotation in xrange(0, numRotations, 1):
			currentNum = rotate(currentNum, numDigits)
			if currentNum in range(lower, upper+1) and originalNum < currentNum:
				numPairs += 1		
	print numPairs