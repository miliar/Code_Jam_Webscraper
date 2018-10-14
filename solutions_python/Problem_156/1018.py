import sys, math

def calcTime(P, Pmax, specialMinutesSpent, minTimeAlreadyFound):
	directTime = Pmax + specialMinutesSpent
	bestTime = min(directTime, minTimeAlreadyFound)
	for i in xrange(1, Pmax/2 + 1, 1):
		newP = P[:]
		newP[Pmax - i - 1] += P[Pmax - 1]
		newP[i - 1] += P[Pmax - 1]
		newPmax = Pmax - 1
		while newPmax > 0 and newP[newPmax - 1] == 0:
			newPmax -= 1
		if newPmax == 1:
			continue
		newTime = calcTime(newP, newPmax, specialMinutesSpent + P[Pmax - 1], bestTime)
		if newTime < bestTime:
			bestTime = newTime
	return bestTime

def solveCase(case, fin, fout):
	D = fin.readline().strip()
	Pstring = fin.readline().strip().split(" ")
	P = 1000*[0]
	Pmax = 0

	for Pi in Pstring:
		Pint = int(Pi)
		P[Pint - 1] += 1
		if Pint > Pmax:
			Pmax = Pint
			
			
	minTime = calcTime(P, Pmax, 0, Pmax)
	
	writeLine(fout, case, minTime)


def writeLine(fout, n, result):
	fout.write("Case #%d: %d\n" %(n, result))

inputFileName = sys.argv[1]

fin = file(inputFileName)
fout = file("%s.out" %(inputFileName.split(".")[0]), "w")

T = eval(fin.readline())

for case in xrange(T):
	solveCase(case + 1, fin, fout)
	
fin.close()
fout.close()
