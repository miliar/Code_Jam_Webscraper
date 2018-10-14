import string

inputFile = "B-large.in"
outputFile = "B-large.out"

fIn = open(inputFile, 'r')
fOut = open(outputFile, 'w')

numTests = fIn.readline()

case = 0
for line in fIn:
	case = case + 1

	numAbvBestResult = 0

	spltLine = line.split(' ')
	numGooglers = int(spltLine[0])
	numSurprises = int(spltLine[1])
	bestResult = int(spltLine[2])
	for x in spltLine[3:]:
		if int(x) < bestResult:
			continue
		if int(x) >= bestResult * 3 - 2:
			numAbvBestResult = numAbvBestResult + 1
		elif int(x) >= bestResult * 3 - 4 and numSurprises > 0:
			numAbvBestResult = numAbvBestResult + 1
			numSurprises = numSurprises - 1
	
	fOut.write("Case #" + str(case) + ": " + str(numAbvBestResult) + "\n")
fIn.close()
fOut.close()

