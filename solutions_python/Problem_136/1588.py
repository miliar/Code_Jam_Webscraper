# -*- coding: utf8 -*-
import os
import sys

def solve(c, f, x, curRate):
	if (x <= c):
		return x / curRate;
	if (x / curRate > (c/curRate + x/(curRate+f))):
		return c/curRate + solve(c, f, x, curRate+f);
	return x/curRate;

def solve2(c, f, x, curRate):
	if (x <= c):
		return x / curRate;
	
	timeUsed = 0.00;
	isContinue = True;
	
	while(True):
		if (x / curRate > (c/curRate + x/(curRate+f))):
			timeUsed = timeUsed + c/curRate;
			curRate = curRate + f;
		else:
			break;
	return timeUsed + x / curRate;

if __name__ == "__main__":
	#input = open("b-sample.txt", "r")
	input = open("b-large.txt", "r")
 	output = open("output-large2.txt", "w")
	
	caseMax = int(input.readline());
	
	for caseCounter in range(caseMax):
		nums = map(float, input.readline().split());
		
		strResult = "%.7f" % solve2(nums[0], nums[1], nums[2], 2);
		#print nums;
		#strResult = "1";
		
		strCase = "Case #%d: " % (caseCounter + 1);
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("Done");