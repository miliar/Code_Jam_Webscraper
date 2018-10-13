#!/usr/bin/python

import sys

def processCase(case,matrix,rows,columns):
	# *** BEGIN CODE PROCESSING CASE ***

	for x in range(rows):
		for y in range(columns):
			if matrix[x][y]=='#':
				if x==rows-1:
					return False 
				if y==columns-1:
					return False
				if matrix[x+1][y]!='#':
					return False
				if matrix[x][y+1]!='#':
					return False
				if matrix[x+1][y+1]!='#':
					return False
				matrix[x][y]="/"
				matrix[x+1][y]="\\"
				matrix[x][y+1]="\\"
				matrix[x+1][y+1]="/"
			 
	# *** END CODE PROCESSING CASE ***
	return True

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
	rows=int(caseInput.split()[0])	
	columns=int(caseInput.split()[1])	

	matrix=[]
	for itr in range(rows):
		caseInput=sys.stdin.readline().split()[0]
		row=[]
		for char in range(len(caseInput)):
			row.append(caseInput[char])
		matrix.append(row)


	# *** END CODE READING CASE ***

	print "Case #"+str(case)+": "
	solution=processCase(case,matrix,rows,columns)
	if solution==False:
		print "Impossible"
	else:
		for itr in range(rows):
			salida=""
			for itr2 in range(columns):
				salida=salida+matrix[itr][itr2]
				#print matrix[itr][itr2]
			print salida	

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

