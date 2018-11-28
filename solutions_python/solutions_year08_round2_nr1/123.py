import sys
import time
import os

fileObj=file(sys.argv[1],'r')
outfile=file('out.txt','w')

numCases=float(fileObj.readline())

for caseNum in range(numCases):

	n,A,B,C,D,X0,Y0,M=fileObj.readline().split()
	A=float(A)
	B=float(B)
	C=float(C)
	D=float(D)
	X0=float(X0)
	Y0=float(Y0)
	M=float(M)
	n=float(n)

	X=X0
	Y=Y0
	i=1

	XList=[]
	YList=[]
	coords=[]
	print X,Y
	XList.append(X)
	YList.append(Y)
	coords.append([X,Y])
	while i  < n:
		X = (A*X+B) % M
		Y = (C*Y+D) % M
		#print X,Y
		coords.append([X,Y])
		XList.append(X)
		YList.append(Y)
		i+=1

	#print coords

	count=0
	found=[]
	j=0
	k=0
	l=0

	i=0	
	found=[]
	while i < len(coords):
		x1,y1=coords[i]
		j=i+1
		while j < len(coords):
			#print "J %s" % j
			x2,y2=coords[j]
			k=j+1
			while k < len(coords):
				#print "K %s" % k
				x3,y3 = coords[k]
				Tx=(x1+x2+x3)/3
				Ty=(y1+y2+y3)/3
				if not Tx%1 and not Ty%1:
					#print x1,x2,x3,[Tx,Ty]
					#print y1,y2,y3,[Tx,Ty]
					#if [Tx,Ty] not in found:# and [Tx,Ty] in coords:
						#print [Tx,Ty]
					found.append([Tx,Ty])
					#	coords.remove
				k+=1
			j+=1
		#print "I %s" % i
		i+=1
	result=len(found)

	text="Case #%s: %s" % (caseNum+1,result)
	print text
	outfile.write(text+"\n")
