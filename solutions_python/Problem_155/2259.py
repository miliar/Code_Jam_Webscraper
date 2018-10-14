def Input(filePath):
	input = open(filePath, "r")
	testCases = input.readlines()
	
	cases = []
	for lineNo in range(len(testCases)):
		#for ever line
		wordsInLine = testCases[lineNo].split(" ")
		cases.append(wordsInLine)
		
	return cases

def solveCase(numOfElem, audience):
	friendsAdded = 0
	peopleTotal = 0
	
	for shynessLvl in range(numOfElem):
		#no point in add people if their is no one at the shyness level
		if int(audience[shynessLvl]) != 0:
			if(peopleTotal >= shynessLvl):
				peopleTotal += int(audience[shynessLvl])
			else:
				#need to add some people
				friendsNeeded = shynessLvl - peopleTotal
				peopleTotal += friendsNeeded
				friendsAdded += friendsNeeded
			
				#next add the people with the extreme shyness level
				peopleTotal += int(audience[shynessLvl])

	return friendsAdded
	
#entry point	
def main():
	cases = Input("A-large.in")
	output = open("opera.out", "w")
	for caseNo in range(1,int(cases[0][0]) + 1):
		#cases[caseNo][wordNo]
		solution = solveCase(int(cases[caseNo][0]) + 1, cases[caseNo][1])
		
		output.write("Case #" + str(caseNo) + ": " + str(solution) + "\n")
		
	output.close()
main()