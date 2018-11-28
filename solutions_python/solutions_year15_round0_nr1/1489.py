import sys	

def solveCase(case, f, fout):
	Smax, people = f.readline().strip().split(" ")
	Smax = int(Smax)
	peopleStanding = 0
	nFriends = 0
	for Si in xrange(Smax + 1):
		nPeople = int(people[Si])
		if Si <= peopleStanding:
			peopleStanding += nPeople
		else:
			addFriends = Si - peopleStanding
			nFriends += addFriends
			peopleStanding += addFriends + nPeople
	writeLine(fout, case, nFriends)

def writeLine(fout, n, result):
	fout.write("Case #%d: %d\n" %(n, result))

inputFileName = sys.argv[1]

f = file(inputFileName)
fout = file("%s.out" %(inputFileName.split(".")[0]), "w")

T = eval(f.readline())

for case in xrange(T):
	solveCase(case + 1, f, fout)
	
f.close()
fout.close()
