#!/usr/bin/env python
import math
import numpy as np

textfile = open("small.in");
lines = [line.strip() for line in textfile]
textfile.close()

numCases = int( lines[0])
l = 1;
cases = np.empty((numCases,4,4))
for i in range(0,numCases,1):
	for r in range(0,4,1):
		for c in range(0,4,1):
			charlist = list(lines[l])
			if(charlist[c] == 'O'):
				cases[i][r][c] = 0
			elif(charlist[c] == 'X'):
				cases[i][r][c] = 5
			elif(charlist[c] == 'T'):
				cases[i][r][c] = 7
			else:
				cases[i][r][c] = 1000
				 
		l = l + 1
	l = l + 1		



ansO = "Case #{no}: O won\n".format(no = i)
ansX = "Case #{no}: X won\n".format(no = i)
ansNC = "Case #{no}: Game has not completed\n".format(no = i)
ansD = "Case #{no}: Draw\n".format(no = i)
#sum = 0 or 7  or 20 or 22 we have a winner O and X
#sum > 1000 we have empty slot
#sum < 1000 and no winner we have draw
textfile = open("small.out","w");
for i in range(0,numCases,1):
	hasempty = False;
	Owon = False;
	Xwon = False;
	for x in range(0,4,1):
		rowsum = (cases[i][x][0] + cases[i][x][1] + cases[i][x][2] + cases[i][x][3]) 
		colsum =  cases[i][0][x] + cases[i][1][x] + cases[i][2][x] + cases[i][3][x]
		if (rowsum == 0 or rowsum == 7 or colsum == 0 or colsum == 7):
			Owon = True
		elif (rowsum == 20 or rowsum == 22 or colsum == 20 or colsum == 22):
			Xwon = True
		elif (rowsum > 999 or colsum > 999):
			hasempty = True
		
	diagsum1 = cases[i][0][0] + cases[i][1][1] + cases[i][2][2] + cases[i][3][3]	
	diagsum2 = cases[i][0][3] + cases[i][1][2] + cases[i][2][1] + cases[i][3][0]
	if (diagsum1 == 0 or diagsum2 == 0 or diagsum1 == 7 or diagsum2 == 7):
		Owon = True
	elif (diagsum1 == 20 or diagsum2 == 20 or diagsum1 == 22 or diagsum2 == 22):
		Xwon = True
	elif (diagsum1 > 999 or diagsum2 > 999):
		hasempty = True
	if Owon:
		print "Case #{no}: O won\n".format(no = i+1)
		textfile.write("Case #{no}: O won\n".format(no = i+1))
	elif Xwon:
		print "Case #{no}: X won\n".format(no = i+1)
		textfile.write("Case #{no}: X won\n".format(no = i+1))
	elif hasempty:
		print "Case #{no}: Game has not completed\n".format(no = i+1)
		textfile.write("Case #{no}: Game has not completed\n".format(no = i+1))
	else:
		print "Case #{no}: Draw\n".format(no = i+1)
		textfile.write( "Case #{no}: Draw\n".format(no = i+1))
			

textfile.close()
