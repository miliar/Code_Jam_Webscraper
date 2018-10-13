import sys

fileName = sys.argv[1]
grid = [[0 for x in range(4)] for x in range(4)]
guess = [0 for x in range(2)]
hashTable = [0 for x in range(17)]
def main():
	with open(fileName) as FileReader:
		testCases = int(FileReader.readline())
		for caseIndex in range(1, testCases + 1):
			flag = False
			counter = 0
			solutionIndex = 0
			for index in range(len(hashTable)):
				hashTable[index] = 0
			for shuffle in range(2):
				guess[shuffle] = int(FileReader.readline()) - 1
				for index in range(4):
					grid[index] = [int(x) for x in FileReader.readline().split()]
				for number in grid[guess[shuffle]]:
					hashTable[number] += 1
			for index in range(len(hashTable)):
				if hashTable[index] > 1:
					solutionIndex = index
					counter += 1
			if counter == 0:
				print "Case #" + str(caseIndex) + ": Volunteer cheated!"
			elif counter == 1:
				print "Case #" + str(caseIndex) + ": " + str(solutionIndex)
			else:
				print "Case #" + str(caseIndex) + ": Bad magician!"

main()