#!/usr/bin/python
import sys 

def findIntersection(A,B):
	#print A, B 
	det = A[0]*B[1] - B[0]*A[1]	
	#print det 
	
	if(det == 0):
		return(0)
	
	else:
		x = float(B[1] * A[2] - A[1] * B[2])/float(det)
		y = float(A[0] * B[2] - B[0] * A[2])/float(det)
	
		#print x,y 
		if(x>=5 and x<=10):
			return(1)
		else:
			return(0)	
	
		
		
def process():
	N = int(sys.stdin.readline().strip())
	
	X1 = 5
	X2 = 10
	B = -5	
	linePoints = []
	for i in range(N):
		Y = map(int, (sys.stdin.readline().strip().split(" ")))
		A = Y[1] - Y[0]
		C = A*5+B*Y[0]
		#print A, C 

		linePoints.append([A,B,C]) 

	count = 0
	
	for i in range(len(linePoints)):
		for j in range(i):
			p1 = linePoints[i]
			p2 = linePoints[j]
			count += findIntersection(p1,p2)
			
	return(count)
				

if(__name__=="__main__"):
	nTestCases = int(sys.stdin.readline().strip())	
	
	for i in range(1,nTestCases+1):
                string = "Case #" + str(i) + ": "
                print string + str(process())

	
