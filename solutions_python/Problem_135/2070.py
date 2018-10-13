formatString = "Case #{0}: {1}"

def main():
	with open("test.in") as f:
		content = f.readlines()

	testCasesCount = int(content[0])

	content = content[1:]

	for testCount in xrange(testCasesCount):
		firstGuess = int(content[testCount * 10])
		secondGuess = int(content[testCount * 10 + 5])
		firstRow = [int(x) for x in content[testCount * 10 + firstGuess].split(' ')]
		secondRow = [int(x) for x in content[testCount * 10 + 5 + secondGuess].split(' ')]
		checkResults(testCount + 1, firstRow, secondRow)

def checkResults(testCount, firstRow, secondRow):
	result = -1
	for x in firstRow:
		for y in secondRow:
			if x == y:
				if result == -1:
					result = x
				else:
					print str.format(formatString, testCount, "Bad magician!")
					return
	if result != -1:
		print str.format(formatString, testCount, str(result))
	else:
		print str.format(formatString, testCount, "Volunteer cheated!")

if __name__ == "__main__":
	main()
