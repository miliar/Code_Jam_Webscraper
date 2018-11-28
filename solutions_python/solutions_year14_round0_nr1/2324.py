# Google Code Jam 2014
# Qualification Round
# Problem A: Magic Trick
#
# Kevin Yap (@iKevinY)
# http://kevinyap.ca

if __name__ == '__main__':
    inputFile = file("A-small-attempt0.in.txt")
    outputFile = file("output.txt", "w+")
    testCases = int(inputFile.readline())

    cards1, cards2 = None, None

    for i in range(0, testCases):
    	firstLine = int(inputFile.readline())
    	for n in range(0, 4):
    		if n == firstLine - 1:
    			cards1 = [int(x) for x in inputFile.readline().split()]
    		else:
    			inputFile.readline()

    	secondLine = int(inputFile.readline())
    	for n in range(0, 4):
    		if n == secondLine - 1:
    			cards2 = [int(x) for x in inputFile.readline().split()]
    		else:
    			inputFile.readline()

    	# Print output to file
    	outputFile.write("Case #{0}: ".format(i + 1))

    	# Returns true for common member
    	if any([card in cards1 for card in cards2]):
    		common = []
    		for n in range(0, len(cards1)):
    			for m in range(0, len(cards2)):
    				if cards1[n] == cards2[m]:
    					common.append(cards1[n])

    		if len(common) == 1:
    			outputFile.write("{0}\n".format(str(common[0])))
    		else:
    			outputFile.write("Bad magician!\n")
    	else:
    		outputFile.write("Volunteer cheated!\n")

