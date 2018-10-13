
def solve(l):
	diffs = [max(l[i - 1]-x,0) for i, x in enumerate(l)][1:]
	m1 = sum(diffs)
	m = max(diffs)
	m2 = sum([min(x, m) for x in l[:-1]]) 
	return [m1,m2]

#inFile =  open(str(sys.argv[1]), 'r')
fileName = 'A-small-attempt0'
fileName = 'A-large'
#fileName = 'B-small-attempt0'
inFile = open(fileName + '.in', 'r')
outFile = open(fileName + '.out', 'w')

nextLine = inFile.readline()
nextLine = inFile.readline()
i = 0
while (nextLine != ""):
	i = i + 1
	#print i
	#s = int(nextLine[:-1].split(' '))
	nextLine = inFile.readline()
	m = nextLine[:-1].split(' ')
	l = [int(x) for x in m]
	m = solve(l)
	nextLine = inFile.readline()
	#for j in range(repeat):
	#	s = s + nextLine
	#r = solve(s,repeat)
	outFile.write('Case #{}: {} {}\n'.format(i,m[0],m[1]))

inFile.close()
outFile.close()	

