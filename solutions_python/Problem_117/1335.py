import os
import re
import sys
import time

inputFile = "E:/Workspaces/codeJam/B-large.in" 
outputFile = "E:/Workspaces/codeJam/output.txt"
file = open(inputFile, "r")
fileout = open(outputFile, "w")


#ALGORITHME
def resolve(case, n, m, count):
	for i in range(0, n):
		for j in range(0, m):
			a = case[i][j]
			columnOk = True
			lineOk = True
			
			#Check Column
			for k in range(0, n):
				if case[k][j] > a:
					columnOk = False
					break
					
			#Check Line
			for k in range(0, m):
				if case[i][k] > a:
					lineOk = False
					break
			
			if not lineOk and not columnOk:
				return False
	return True
			

#READ COUNT
countCase = int(file.readline())
print("\nCase count: %d" % countCase)


# READ
for i in range(0, countCase):
	line1 = file.readline().split(" ")
	N = int(line1[0])
	M = int(line1[1])
	caseTemp = []
	
	for j in range(0, N):
		line2 = file.readline().split(" ")
		caseLine = []
		for k in range(0, M):
			caseLine.append(int(line2[k]))
		caseTemp.append(caseLine)
	
	answer = resolve(caseTemp, N, M, i)
	if answer :
		fileout.write(("Case #{0}: YES\n").format((i+1)))
	else:
		fileout.write(("Case #{0}: NO\n").format((i+1)))
	

	
file.close()
fileout.close()
	

	
	