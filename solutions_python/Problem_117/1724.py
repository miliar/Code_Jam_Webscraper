#!/usr/bin/env python
import sys
sys.path.append("../")
import fileHandler

##################################################
# Lecture fichier
ifile = fileHandler.Fichier("B-small-attempt1.in")
ofile = fileHandler.Fichier("Bsmall1321.out")
text = ifile.read()
inputs= text.split('\n')
# Fin lecture
##################################################

T = int(inputs[0])
##################################################
def getMatrix(inputs,startIndex,N,M):
	mat = [[None for i in range(M)] for j in range (N)]
	for i in range(N):
		values = inputs[startIndex + i].split(' ')
		for j in range(M):
			mat[i][j] = int(values[j])
	return mat

def canCut(array,height):
	for i in range(len(array)):
		if(array[i] > height):
			return i
	return -1

def getColumn(matrix, i):
    return [row[i] for row in matrix]

def solve(matrix,N,M):
	canDo = True
	for i in range(N):
		h = matrix[i][0]
		H = canCut(matrix[i],h)
		if(H >= 0):
			for j in range(M):
				if (canCut(getColumn(matrix,j),matrix[i][j]) >=0):
					return False
		else:
			for j in range(M):
				if (matrix[i][j] < h and (canCut(getColumn(matrix,j),matrix[i][j]) >=0)):
					return False
	return True 
			
response = ""
nextIndex = 1
for i in range(T):
	size = inputs[nextIndex].split(' ')
	N = int(size[0])
	M = int(size[1])
	nextIndex += 1
	result = solve(getMatrix(inputs,nextIndex,N,M),N,M)
	nextIndex += N
	if(result):
		result = "YES"
	else:
		result = "NO"
	response = response + "Case #"+str(i+1)+": "+result+"\n"	
print(response)
ofile.write(response)
