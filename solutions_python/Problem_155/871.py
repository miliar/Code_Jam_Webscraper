#
# Google Code Jam 2015
# Roaund 0: A. Standing Ovation
# submission by EnTerr
#

'''

T = #test cases to follow. 
Each consists of one line with Smax, ... followed by a string of Smax + 1 single digits. 
The kth digit of this string (starting from 0) = how many people  have shyness level k.

Input 
4
4 11111
1 09
5 110011
0 1
 	
Output 
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0

'''



import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def getNumShills(shys):
	numShills = 0
	numClapping = 0
	for lvl, num in enumerate(shys):
		if lvl > numClapping:
			recruit = lvl - numClapping 
			numShills += recruit
			numClapping += recruit
		numClapping += num
	
	return numShills
	

#clk = clock()

for caseNo in xrange(1, int(input())+1):
    shys = map(int, list(input().split()[1]))
#    print >>sys.stderr, caseNo
    print 'Case #%d:' % caseNo, getNumShills(shys)
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

