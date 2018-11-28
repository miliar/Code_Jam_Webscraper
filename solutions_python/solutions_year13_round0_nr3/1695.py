#not optimized at all
class FileManager:
	handler = False;

	def open(self, file):
		self.handler = open( file, 'r' )

		if self.handler == False:
			return False

		return True

	def getLine( self ):
		if self.handler == False:
			return False

		line = self.handler.readline()

		if not line:
			return False

		return line

	def close( self ):
		if self.handler == False:
			return True;

		close( self.handler )

		return True

def isPalindrome(s):
	st = str(s)
	r = int(st[::-1])
	return s == r

# made with the previous version
#this table was made with the code that is commented below (Used for the small sample)
pm = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004]

FM = FileManager()
#FM.open( "./sample.txt" )
#FM.open( "./C-small-attempt0.in" )
FM.open( "./C-large-1.in" )

numberOfCases = int( FM.getLine() )

from math import *

#for currentCaseIndex in xrange(1, numberOfCases+1, 1):
	#( requestedMin, requestedMax ) = FM.getLine().split(" ")
	#requestedMin = RM  = int(requestedMin)
	#requestedMax = RMX = int(requestedMax)
	#x = 0
	#fairAndSquare = 0
	#requestedMax = int( ceil(sqrt( requestedMax )) )
	#requestedMin = int( ceil(sqrt( requestedMin )) )
#	
	#for x in xrange( requestedMin, requestedMax+1 ):
		#npow = int(x **2)
#
		#if( npow > RMX or npow < RM ):
			#break
#
		#if isPalindrome( (x) ):
			#if( isPalindrome(( npow ))):
				#print x, npow
				#fairAndSquare += 1
#		
	#print "Case #%u: %u" % ( currentCaseIndex, fairAndSquare )

for currentCaseIndex in xrange(1, numberOfCases+1, 1):
	( requestedMin, requestedMax ) = FM.getLine().split(" ")
	requestedMin = RM  = int(requestedMin)
	requestedMax = RMX = int(requestedMax)
	fairAndSquare = 0
	for z in xrange(0, len(pm)):
		
		if( pm[z] >= requestedMin and pm[z] <= requestedMax ):
			fairAndSquare += 1
		
		if( pm[z] > requestedMax ):
			break

	print "Case #%u: %u" % ( currentCaseIndex, fairAndSquare )
