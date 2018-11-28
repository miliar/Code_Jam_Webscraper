#!/usr/bin/env python 
import sys 

LabelMatrix = []
newMatrix = []
Matrix = []

sys.setrecursionlimit(100000)

def processInput(Matrix,W,H):
	for i in range(W):
		temp = []
		for j in range(H):
			temp.append([])
		newMatrix.append(temp)

			
	indexEntry = [(-1,0),(0,-1),(0,1),(1,0)]
	
	for i in range(W):
		tmp = []
		for j in range(H):
			temp = []
			if(i-1>=0 and j>=0):
				temp.append(int(Matrix[i-1][j]))
			else:
				temp.append(sys.maxint)
			
		
			if(i>=0 and j-1>=0):
				temp.append(int(Matrix[i][j-1]))
			else:
				temp.append(sys.maxint)
			
			try:
				temp.append(int(Matrix[i][j+1]))
			except:
				temp.append(sys.maxint)
		

			try:	
				temp.append(int(Matrix[i+1][j]))
			except:
				temp.append(sys.maxint)
			

							
				
			#if(i==1 and j ==2):
			#	print temp

			# find minimum index 
			minm = min(temp)
			if(minm < int(Matrix[i][j])):
				index = temp.index(minm)
				entry = indexEntry[index]
				#print (i,j)
				#print (i+entry[0],j+entry[1])
				try:	
					if((i,j) not in newMatrix[i+entry[0]][j+entry[1]]):
						newMatrix[i+entry[0]][j+entry[1]].append((i,j))
					if((i+entry[0],j+entry[1]) not in newMatrix[i][j]):
						newMatrix[i][j].append((i+entry[0],j+entry[1]))
				except:
					pass 
				
		
				#print entry 
				#print i,j 
	
	
	#print newMatrix	


def setNeighBour(i,j,label):
	LabelMatrix[i][j] = label 
	#print sys.getrecursionlimit()
	array = newMatrix[i][j]

	for val in array:
		if(LabelMatrix[val[0]][val[1]]=='1'):
			setNeighBour(val[0],val[1],label)
	

		

def parsefile(infile):
	fp = open(infile)
	data = fp.readline()
	nTestCases = int(data.strip())
	

	cnt = 1
	for i in range(nTestCases):
		global newMatrix
		global LabelMatrix 
		global Matrix

		newMatrix = []
		LabelMatrix = []
		Matrix = []

		data = fp.readline()
		fields = data.split(" ")
		W = int(fields[0])
		H = int(fields[1])
		#print W,H

		for i in range(W):
			data = fp.readline()	
			ff = data.strip().split(' ')
			Matrix.append(ff)
		#print Matrix
		processInput(Matrix,W,H)			
		#print newMatrix
		label()
		print "Case #"+str(cnt)+":"
		cnt += 1
		printmatrix()


def printmatrix():
	for i in range(len(LabelMatrix)):
		print " ".join(LabelMatrix[i])	
		

		

	
def label():
	global LabelMatrix

	for i in range(len(Matrix)):
		temp = []
		for j in range(len(Matrix[0])):
			temp.append("1")
		LabelMatrix.append(temp)
	
	#print LabelMatrix	
	LabelMatrix[0][0] = 'a'
	setNeighBour(0,0,'a')

	#print LabelMatrix
	
	chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	count = 1
	for i in range(len(LabelMatrix)):
		for j in range(len(LabelMatrix[0])):
			if(LabelMatrix[i][j] == '1'):
				LabelMatrix[i][j] = chars[count]
				setNeighBour(i,j,chars[count])
				count += 1
				#if(count == 26):
				#	count = 0
				
	#print LabelMatrix

	

if(__name__=="__main__"):
	parsefile(sys.argv[1])
	
