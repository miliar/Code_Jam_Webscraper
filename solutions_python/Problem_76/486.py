#
#  TestCandy.py
#  
#
#  Created by FEI LIU .
#  Copyright (c) 2010 ucla. All rights reserved.
#

from Candy import candy 

input = open('C-large.in.txt', 'r')
ouput = open('data_result_large', 'w')
caseNumber = 0
firstLine = 1
lineNo = 1
totalNum = 0
for line in input.readlines():
    if(firstLine):
        caseTotal = line.rstrip()
        firstLine = 0
        continue
	
    lineNo = lineNo + 1
    line = line.rstrip()
    
    if(lineNo % 2 == 0):
      totalNum = int(line)
      continue
    else:
      rstStr = candy(line, totalNum)
#		parts = map(int, line.split(" "))
#		R = parts[0]
#		k = parts[1]
#		N = parts[2]
#		caseNumber += 1
#		continue
      caseNumber += 1	
	#gList = map(int, line.split(" "))
	#N = gList[0]
	#K = gList[1]
	#lightState = snapperChain(N, K)
	#if(lightState == 0):
	#	rstStr = "OFF"
	#else:
	#	rstStr = "ON"
    #rstStr_tmp = botTrust(line)
    #rstStr = str(rstStr_tmp)
      ouput.write("Case #")
      ouput.write(str(caseNumber))
      ouput.write(":" + " " + rstStr + "\n")	

input.close()
ouput.close()	
