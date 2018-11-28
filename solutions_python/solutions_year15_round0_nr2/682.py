from math import ceil

f_in = open('B-large.in')
my_input = f_in.readlines()# Expected output
f_in.close()
#Case #1: 3
#Case #2: 2
#Case #3: 3

debug = False

case_count = int( my_input.pop(0) )
cases = [None]*case_count

for i in range(case_count):
	numNonEmptyPlates = int( my_input.pop(0) )
	pancakeCountAry = map(int, my_input.pop(0).split() )
	if len(pancakeCountAry) != numNonEmptyPlates: raise Exception()
	cases[i] = pancakeCountAry

def largestAfterRemovingI( x, i ):
	x = x[:]
	x.pop(i)
	if len(x) > 0:
		return max(x)
	else:
		return 0

# Make 2D array where:
# one axis is the number of the person who has pancakes initially
# the other is how many times you could divide their pancakes, e.g. 0 for none, 1 for once (meaning divide it into two portions)
# the value of the array is how many minutes you have to add up to
def getMinimumMinutes( pancakeCounts ):
	possibs = [None]*len(pancakeCounts)
	for dinerId in range( len(pancakeCounts) ):
		possibs[dinerId] = [0]*(1000+1)
		dinerOrigPancakes = pancakeCounts[dinerId]
		for pancakeCount in range( dinerOrigPancakes, 1-1, -1):
			# To achieve pancakeCount or more pancakes,
			# you must divide something into n groups...
			# and to make n groups takes n+1 special minutes..
			# e.g.	turning 1 group into 2 is 1 division,
			# 		turning 1 group into 3 is 2 divisions
			div_count = int( ceil( dinerOrigPancakes*1.0 / pancakeCount ) ) - 1
			possibs[dinerId][pancakeCount] = div_count # how many minutes you'd have to wait to use this option

	minutes_possibs = []
	for pancakeCount in range(1,1000+1):
		timeToComplete = pancakeCount
		for dinerId in range( len(pancakeCounts) ):
			specialMinuteCount = possibs[dinerId][pancakeCount]
			timeToComplete += specialMinuteCount

		minutes_possibs.append( timeToComplete )

	return min( minutes_possibs ), possibs



debug = False
	
toReturn = []
for case in cases:
	time, possibs = getMinimumMinutes( case )
	if debug:
		print 'for case: %s' % case
		for x in possibs:
			print x[:10]
		print 'best time: %d' % time
		print '\n\n'
			
	toReturn.append( time )

f_out = open('output.txt', 'w' )
for i, caseResult in enumerate(toReturn):
	toWrite = 'Case #%d: %d\n' % ( i+1, caseResult )
	f_out.write( toWrite )
		
f_out.close()
