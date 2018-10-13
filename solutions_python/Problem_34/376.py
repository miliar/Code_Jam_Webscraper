import re

inFile = open("A-large.in")
line = inFile.readline()

re_str=""

dictionary=[]
testcases=[]

numbers= map(int,line.split())

L = numbers[0]
D = numbers[1]
N = numbers[2]

for i in xrange(0,D):
	dictionary.append( inFile.readline().rstrip('\n') )

for i in xrange(0,N):
	testcases.append( inFile.readline().rstrip('\n') );

inFile.close()

p = re.compile( '\([a-z]+\)+|[a-z]+' )

outFile = open("out.txt", 'w')

casenum = 1
for i in testcases:

	tokens = p.findall(i)
	regstr=""
	matches=0

	for t in tokens:
		if(t[0] == '('):
			regstr = regstr + '[' + t.lstrip('(').rstrip(')') + ']'
		else:
			regstr = regstr + t

	rgx = re.compile(regstr)

	for w in dictionary:
		if( rgx.match(w) ):
			matches = matches + 1

	outFile.write( "Case #" + str(casenum) + ": " + str(matches) + "\n")
	casenum += 1


outFile.close()
