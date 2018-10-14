import sys
from fractions import gcd


f = open('input.txt', 'r')
N = int(f.readline().strip())

def check(n, pd, pg):
	if( pg == 100):
		if(pd < 100):
			return 0
	if(pg == 0):
		if(pd > 0):
			return 0

	x = gcd(pd,100)
	a = pd/x
	b = 100/x
	if(a > n or b > n):
		return 0
	#elif(a < b and pg == 100):
	#	return 0
	#elif():	
	else:
		return 1	 
		
for i in range(0, N):
	case = f.readline().strip().split()
	case = map(int, case)
	#print case
	#poss = False
	poss = check(case[0], case[1], case[2])
	if poss == 1:
		print 'Case #' + str(i+1) + ': Possible'
	else:
		print 'Case #' + str(i+1) + ': Broken'				 
		
