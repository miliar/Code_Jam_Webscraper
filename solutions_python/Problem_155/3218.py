from sys import argv

script, filename = argv

txt = open(filename)

inputfile = txt.readlines()
numCases = int(inputfile[0])

for i in range(1, numCases + 1):
	missingAud = 0
	totalAud = 0
	currentCase = inputfile[i]
	numSi = int(currentCase.split()[0])
	audArray = currentCase.split()[1]
	for si in range (numSi + 1):
		if (si != 0):
			while (totalAud < si):
				missingAud += 1
				totalAud += 1
		totalAud += int(audArray[si])
	print "Case #" + str(i) + ": " + str(missingAud)