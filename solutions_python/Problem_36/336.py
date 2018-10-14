#!/usr/bin/python

def readInput():
	file = open("C-small-attempt0.in")

	lineCount = int(file.readline().rstrip())
	lines = [file.readline().rstrip() for i in range(0, lineCount)]

	return lines

def findText(line, textToFind):
	stack = []

	findLength = len(textToFind)
	lineLength = len(line)

	findPos = 0
	linePos = 0

	findCount = 0

	while findPos != 0 or linePos != lineLength:
		if linePos < lineLength and line[linePos] == textToFind[findPos]:
			findPos += 1

			if findPos == findLength:
				findCount += 1
				findPos -= 1
			else:
				stack.append(linePos)

		linePos += 1

		if linePos >= lineLength and len(stack) != 0:
			findPos -= 1
			linePos = stack.pop() + 1

	return findCount

textToFind = "welcome to code jam"

results = [findText(line, textToFind) for line in readInput()]

case = 1
for result in results:
	print "Case #%s: %04d" % (case, result % 10000)
	case += 1
