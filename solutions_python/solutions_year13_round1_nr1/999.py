import sys
from math import sqrt , floor

def invYo(r,t):
	return (1.0/4.0)*( sqrt(4.0*r**2.0-4.0*r+8.0*t+1.0)-2.0*r +1.0)


def calculateBulls(r,t):
	#~ print invYo(r,t)
	return int(floor(invYo(r,t)))

def main():
	with open(sys.argv[1]) as inFile:
		cases=[]
		N = int(inFile.readline())
		for i in range(N):
			cases.append(map(int,inFile.readline().split()))

	solutions=[]

	for t,r in cases:
		print solutions.append(calculateBulls(t,r))
		#~ break


	print solutions



	


		
	with open(sys.argv[2],'w') as outFile :	
		for index,solution in enumerate(solutions):
			print solution
			outFile.write( 'Case #' + str(index+1) + ': ' + str(solution) + '\n')

if __name__ == "__main__":
    main()
