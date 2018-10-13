from sets import *

inName='A-small-attempt1.in'
outName='out.txt'

# 34 total bases

def maxSymbol( inStr ):
	m=0
	v=""
	for i in inStr:
		if( ord(i) > m ):
			m=ord(i)
			v=i
	return v
	
def minBase( inStr ):
	s = set([])
	for c in inStr:
		if( not(c in s) ):
			s.add( c )
	return s

def genMap( inStr=""):
	d=dict()
	s=set([])
	
	c = inStr[0]
	d[c] = 1
	s.add( c )

	pos=-1
	for i in xrange(len(inStr)):
		if(inStr[i] != c):
			pos=i
			break;
	if( pos==-1 ):
		return d

	#if( pos == -1 )
	d[inStr[pos]] = 0
	s.add( inStr[pos] )
	
	curVal=2
	for i in xrange(pos,len(inStr)):
		if( not(inStr[i] in s ) ):
			s.add(inStr[i])
			d[inStr[i]] = curVal
			curVal += 1
	return d
		


def decToBase( num ):
	if( num >=0 and num < 11 ):
		return str(num)
	else:
		return chr(num+86)

#==============================================================================
caseList=[]
inFile = open(inName,'r')
numCases = map(int,inFile.readline().split())[0]
for i in xrange(numCases):
	caseList.append( inFile.readline().rstrip() )
inFile.close()

#==============================================================================

case=1
outFile=open(outName,'w')

for c in caseList:
	s = minBase( c )
	base = len(s)
	if(base == 1):
		base += 1
	d=genMap(c)
	
	numStr=""
	for i in c:
		numStr += decToBase(d[i])
	outFile.write("Case #" + str(case) + ": " + str(int(numStr,base)) + "\n")
	case += 1
	
outFile.close()


	
	