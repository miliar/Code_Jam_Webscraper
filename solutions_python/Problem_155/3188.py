import sys

""" string sem o valor inicial"""
def standing (input):
	numClap = 0
	friend = 0
	members = input.split(" ")
	shy = int(members[0])+1
	for k in range(0, shy):
		if (numClap >= k):
			numClap += int(members[1][k])
		else:
			friend += 1
			numClap += int(members[1][k])+1
	return friend

""" lê o arquivo, deve passar o arquivo"""
def readInput ():
	inputFile = open(sys.argv[1], 'r')
	outputFile = open('output.txt', 'w')
	test = int(inputFile.readline())
	for i in range(0,test):
		friend = standing(inputFile.readline())
		outputFile.write("Case #" + str((i+1)) + ": " + str(friend) + "\n")
	inputFile.close()
	outputFile.close()

readInput()
