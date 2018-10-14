# -*- coding: utf8 -*-
import os
import sys

def isDistinguishable(num):
	strNum = str(num);
	limit = len(strNum);
	
	if(1 == limit):
		return False;
	elif(2 == limit):
		return strNum[0] != strNum[1];
	
	for idx in range(1, limit):
		if(strNum[0] != strNum[idx]):
			return True;
	
	return False;

if __name__ == "__main__":
	#input = open("C-sample2.txt", "r")
	#input = open("C-small-attempt.in", "r");
	input = open("C-large.in", "r")
	output = open("C-output-large.txt", "w")
	
	caseMax = int(input.readline())
	
	for caseCounter in range(caseMax):
		buf = input.readline();
		buf = buf.split(" ");
		
		numA = int(buf[0]);
		numB = int(buf[1]);

		dictNums = {};
		
		loop = numA;
		digitLen = len(str(numA));
		digitLoop = 0;
		
		while(loop <= numB):
			strNum = str(loop);
			
			for idx in range(len(strNum) - 1):
				strNum = "%s%s" % (strNum[1:], strNum[0]);
				tempNum = int(strNum);
				
				if(False == isDistinguishable(tempNum)):
					continue;
				
				if(tempNum > loop and tempNum <= numB):
					dictNums["%s,%s" %(loop,strNum)] = tempNum;
				
			loop = loop + 1;
		
		strResult = "%d" % len(dictNums);
		
		strCase = "Case #%d: " % (caseCounter + 1);
		
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("done")