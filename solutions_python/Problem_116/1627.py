import fileinput
import sys

def main():
	testCases = int(raw_input())
	#print testCases
	testCount = 1
	while (testCount <= testCases):
		testCase = []
		while (True):
			line = raw_input()
			if (line == ''):
				break
			testCase.append(line)

		result = handleTest(testCase)

		print "Case #%d:" % (testCount),

		if (result == 'X'):
			print "X won"
		if (result == 'O'):
			print "O won"
		if (result == '.'):
			print "Game has not completed"
		if (result == 'T'):
			print "Draw"

		testCount += 1

	return 0

def handleTest(testCase, rotated = False, diag = False):
	emptyNodes = False

	for line in testCase:
		count = {'X': 0, 'O': 0, 'T': 0, '.': 0}

		for char in line:
			if (char == '\n'):
				continue
			count[char] += 1

		#print count
		if (count['.'] > 0):
			emptyNodes = True
		if (count['X'] + count['T'] == 4 and count['X'] > 0):
			return 'X'
		if (count['O'] + count['T'] == 4 and count['O'] > 0):
			return 'O'

	if (rotated == False):
		return handleTest(rotate(testCase), True, False)
	if (diag == False):
		return handleTest(diagon(testCase), True, True)

	if (emptyNodes == True):
		return '.'

	return 'T'

def diagon(testCase):
	newTest = []
	newTest.append(testCase[0][0] + testCase[1][1] + testCase[2][2] + testCase[3][3])
	newTest.append(testCase[0][3] + testCase[1][2] + testCase[2][1] + testCase[3][0])
	return newTest

def rotate(testCase):
	rotated = []
	
	for i in xrange(4):
		newLine = testCase[0][i] + testCase[1][i] + testCase[2][i] + testCase[3][i]
		rotated.append(newLine)

	return rotated

if __name__ == "__main__":
	sys.exit(main())
