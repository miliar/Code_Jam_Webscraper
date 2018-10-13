def __main__(inputFile, output):

	#a bunch of functions.

	mainFile = open(inputFile)
        numCases = mainFile.readline()
        theRest = mainFile.readlines()
	result = CompileOutput(numCases, theRest)
	DeployOutput(result, output)

def CompileOutput( T , cases ):

	resultArr = []
	caseNum = 0
	for case in cases:
		caseNum = caseNum + 1
		# Get the Max "Shyness"
		sep = case.split(' ')
		maxShy = sep[0]
		members = sep[1]
		standing = int(members[0])
		members = members[1:-1]
                shynessLevel = 0
		neededFriends = 0
		for people in members:
			shynessLevel = shynessLevel + 1
			while standing < shynessLevel:
				neededFriends = neededFriends + 1
				standing = standing + 1
			standing = standing + int(people)
		resultArr.append([caseNum,neededFriends])
	return resultArr

def DeployOutput(result, output):

	f = open(output, 'r+')
        for case in result:
		f.write("Case #" + str(case[0]) + ": " + str(case[1]) + "\n")

import sys
__main__(sys.argv[1], sys.argv[2])
