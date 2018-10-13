inputFile = open('A-large.in', 'r')
outputFile = open('output.out', 'w')

numCases = int(inputFile.readline().strip())
lines = [line.strip() for line in inputFile]
lineNumber = 1
for line in lines:
	ints = line.split()
	numPeople = int(ints[0])
	
	people = []
	
	for i in xrange(0,numPeople+1):
		people.append(int(ints[1][i]))
	print "people", people
		
	toBring = 0
	stoodUp = 0
	
	for i in xrange(0,numPeople+1):
		stoodUp += people[i]
		if stoodUp < (i+1):
			stoodUp+=1
			toBring+=1
	
	print "toBring " + str(toBring)
	outputFile.write("Case #"+str(lineNumber)+": "+str(toBring) + "\n")
	lineNumber+=1