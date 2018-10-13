import sys

num_cases = int(sys.stdin.readline())


	
def result(a):	
	a = map(int,a.split())
	area = a[1] * a[2]
	sq = [a[1],a[2]]
	#must be correct number of squares
	if ((area % a[0]) > 0):
		return "RICHARD"
	if (a[0] == 1):
		#impossible to lose
		return "GABRIEL"
	if (a[0] == 2): 
		#if the area is right he will always win
		return "GABRIEL"	
	if (a[0] == 3):
		#if either side is 1 a corner piece will lose
		if (a[1] == 1) or (a[2] == 1):
			return "RICHARD"
		#2x3  - always possible
		#3x3 - always possible			
		#4x3 - always possible
		return "GABRIEL"	
		
	if (a[0] == 4):
		#one side must be 4 or the 4 long won't work
		if (a[1] < 4) and (a[2] < 4):
			return "RICHARD"
		#l shape won't fit
		if (a[1] == 1) or (a[2] == 1):
			return "RICHARD"
		#t shape leaves gap
		if (a[1] == 2) or (a[2] == 2):
			return "RICHARD"
		#3x4 / 4x4 Always Possible
		return "GABRIEL"	
	return "NO"

	
for i in range(1,num_cases+1):	
	print "Case #" + str(i) + ": " + result(sys.stdin.readline())
	#print "-----------"
