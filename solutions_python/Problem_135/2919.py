def run_magic_trick():
	fileName = 'A-small-attempt0'
	resultString = ""
	with open(fileName + ".in") as f:
		numCases = int(f.readline()) + 1
		for case in range(1, numCases):
			firstRowIndex = int(f.readline()) - 1
			firstArrangement = []
			secondArrangement = []
			for rownum in range(0, 4):
				firstArrangement.append(f.readline())
			secondRowIndex = int(f.readline()) - 1
			for rownum in range(0, 4):
				secondArrangement.append(f.readline())

			firstRow = firstArrangement[firstRowIndex].split()
			secondRow = secondArrangement[secondRowIndex].split()
			resultSet = set(firstRow).intersection(set(secondRow))
			result = ""
			setLength = len(resultSet)
			if setLength == 1:
				result = str(resultSet.pop())
			elif setLength > 1:
				result = "Bad magician!"
			else:
				result = "Volunteer cheated!"
			resultString += "Case #" + str(case) + ": " + result + "\n"

	outputFile = open(fileName + ".out", "w")
	outputFile.write(resultString)
	outputFile.close()

if __name__ == '__main__': 
	import sys
	run_magic_trick()