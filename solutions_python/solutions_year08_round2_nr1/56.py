#!/usr/bin/python

import sys

def handle_case(n,A,B,C,D,x0,y0,M):
	
	(X,Y) = (x0,y0)
	Points = [(X,Y)]
	X = (A*X+B) % M
	Y = (C*Y+D) % M
	Points.append((X,Y))

	counter = 0
	for i in range(1,n-1):
		X = (A*X+B) % M
		Y = (C*Y+D) % M
		for j in range(len(Points)):
			for k in range(j+1,len(Points)):
				P1 = Points[j]
				P2 = Points[k]
				P3 = (X,Y)
				if (P1[0]+P2[0]+X)%3==0 and (P1[1]+P2[1]+Y)%3==0:
					counter +=1
		Points.append((X,Y))
	return counter

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(n,A,B,C,D,x0,y0,M) = map(int,fsock.readline().rstrip("\n").split(" "))
		print "Case #%d: %d" % (case, handle_case(n,A,B,C,D,x0,y0,M))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

