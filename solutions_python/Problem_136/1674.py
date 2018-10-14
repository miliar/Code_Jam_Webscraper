'''
	12/04/2014
	Google Code jam
	Problem 2: Cookie Clicker Alpha
'''

def solve(C, F, X):
	elapsed = 0.0 		#time already spent
	cps = 2.0			#coockies per second
	
	while X/cps > (C/cps)+X/(cps+F) : #add a factory while it's convenient
		elapsed += C/cps		
		cps += F

	elapsed += X/cps 
	return elapsed
	

if __name__=='__main__':
	t = int( input() )
	for x in range(1, t+1):
		(C, F, X) = [float(i) for i in input().split()]
		S = solve(C, F, X)
		print("Case #" + str(x) + ": " + str(S))