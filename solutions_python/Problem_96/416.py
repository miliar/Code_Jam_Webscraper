# -*- coding: utf8 -*-
import os
import sys

if __name__ == "__main__":
	#input = open("B-sample.txt", "r")
	#input = open("B-small-attempt.in", "r");
	input = open("B-large.in", "r")
	output = open("B-output-large.txt", "w")
	
	caseMax = int(input.readline())
	
	for caseCounter in range(caseMax):
		buf = input.readline();
		buf = buf.split(" ");
		
		numOfGglers = int(buf[0]);
		numOfSpriss = int(buf[1]);
		cutlineAvg = int(buf[2]);
		
		numOfBest = 0;
		numOfClose = 0;
		numOfEnough = 0;
		
		remainingSuprises = numOfSpriss;
		
		for idx in range(numOfGglers):
			score = int(buf[3 + idx]);
			#scoreAvg = score / 3;
			deductedScore = score - cutlineAvg;
			#deductedScoreAvg = deductedScore / 2;
			deductedScore2 = deductedScore - cutlineAvg + 1;
			
			if(0 > deductedScore):
				continue;
			if(deductedScore2 >= cutlineAvg - 1):
				numOfBest = numOfBest + 1;
			elif(deductedScore2 >= cutlineAvg - 3):
				if(remainingSuprises > 0):
					remainingSuprises = remainingSuprises - 1;
					numOfBest = numOfBest + 1;
							
		strResult = "%d" % (numOfBest);
		
		strCase = "Case #%d: " % (caseCounter + 1);
		
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("done")