import re

inName="C-small-attempt0.in"
outName="out.txt"

theString='welcome to code jam'
size = 19


class TestCase:

	def __init__( self, testStr="" ):
		self.testStr = testStr
		self.length = len(self.testStr)
		self.numStrings = 0

		
	def getCharPositions(self, localPos=0, c=""):
		l=[]
		for i in xrange(localPos,self.length):
			if( self.testStr[i] == c):
				l.append( i )
		return l

	def run(self):
		localPos = 0
		curChar = 0
		self.numStrings = 0
		
		# Get initial list of starting chars
		initList = self.getCharPositions(localPos, theString[curChar])
		self.recurse( initList, curChar+1 )
		
	def recurse(self, list, curChar):
		if( len(list) == 0 ):
			return
		
		for localPos in list:
			newList = self.getCharPositions( localPos, theString[curChar] )
			if( curChar == 18 and len(newList)>0 ):
				self.numStrings += len(newList)
			else:
				self.recurse( newList, curChar+1 )

	# yes, I know this is sloppy, but I have little time to work with here :)
	def getStrCount(self):
		if( len(str(self.numStrings)) >= 4 ):
			s = str(self.numStrings)
			l = len(s)-1
			return s[l-4] + s[l-3] + s[l-2] + s[l-1]
		else:
			return str(self.numStrings).zfill(4)
			
		
# =============================================================================
# (STEP 1) LOAD DATA
# =============================================================================

inFile = open(inName,'r')
cases = map(int,inFile.readline().split())[0]
caseList = []
for i in xrange(0,cases):
	c = TestCase(inFile.readline())
	caseList.append( c )
inFile.close()

# =============================================================================
# (STEP 2) PROCESS DATA
# =============================================================================

for c in caseList:
	c.run()
	
# =============================================================================
# (STEP 3) OUTPUT RESULTS
# =============================================================================

outFile = open(outName,'w')
caseNum = 1
for c in caseList:
	outFile.write("Case #" + str(caseNum) + ": " + c.getStrCount() + "\n")
	caseNum += 1
outFile.close()

	