import re

def recy(m,n):
	M = str(m)
	N = str(n)
	for i in range(0,len(M)):
		if M.lstrip('0')==N.lstrip('0'):
			#print m,n,"     ",M,N
			return True
		M= M[1:] + M[0]
	return False

prob =0
input= open("input.txt")
numProbs=input.readline()
for line in input:
	prob=prob+1
	output=0
	A,B=line.split()
	A = int(A)
	B = int(B)

	for n in range(A,B):
		for m in range(n+1,B+1): #m>n
			if recy(m,n):
				output=output+1

	print "Case #"+str(prob)+": "+str(output)