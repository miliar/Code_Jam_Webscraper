
textFile = open("A-large.in", "r")
outFile = open("A.in", "w")
caseNumber = int(textFile.readline())
for index in xrange(caseNumber):
	line = textFile.readline()
	maxShyness, people = line.split(' ')
	peopleList = list(people)
	peopleList = peopleList[:-1]

	present = 0
	needs = 0
	i = 0

	for SiCount in peopleList:
		if i <= present:
			present += int(SiCount)
		else: 
			remainder = i - present
			needs +=  remainder
			present += int(SiCount) + remainder


		i += 1

	outFile.write("Case #" + str(index + 1) + ": " + str(needs) + "\n")



	numberTestCases = 0


outFile.close()

