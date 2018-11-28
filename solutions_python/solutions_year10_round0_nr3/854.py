#
#  testAlienNumber.py
#  
#
#  Created by FEI LIU on 2/25/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

from ThemePark import themePark 

input = open('C-small-attempt0.in', 'r')
ouput = open('data_result_small', 'w')
caseNumber = 0
firstLine = 1
lineNo = 1
for line in input.readlines():
	if(firstLine):
		caseTotal = line.rstrip()
		firstLine = 0
		continue
	lineNo += 1
	line = line.rstrip()
	if(lineNo%2 == 0):
		parts = map(int, line.split(" "))
		R = parts[0]
		k = parts[1]
		N = parts[2]
		caseNumber += 1
		continue
	
	gList = map(int, line.split(" "))
	dollar = themePark(R, k, gList, N)
	ouput.write("Case #")
	ouput.write(str(caseNumber))
	ouput.write(":"+" "+ str(dollar)+"\n")				

input.close()
ouput.close()	
