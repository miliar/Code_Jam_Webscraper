'''
	12/04/2014
	Google Code jam
	Problem 1: Magic Trick
'''

def solve(a1,g1,a2,g2,x):
	pos = 0 #number of possible solution
	sol = 0
	
	for num in g1[a1-1]:
		if (num in g2[a2-1]):
			pos += 1
			sol = num
	
	if pos==1: #one solution
		print( "Case #" + str(x) +": " + str(sol) )
	elif pos==0:
		print( "Case #" + str(x) +": " + "Volunteer cheated!" )
	else:
		print( "Case #" + str(x) +": " + "Bad magician!" )
		
	

if __name__=='__main__':
	t = int( input() )
	for x in range(1, t+1):
		a1 = int( input() )
		g1 = []
		for i in range(4):	
			g1.append( [int(x) for x in input().split()] )
		a2 = int( input() )
		g2 = []
		for i in range(4):
			g2.append( [int(x) for x in input().split()] )
		
		
		solve(a1, g1, a2, g2, x)