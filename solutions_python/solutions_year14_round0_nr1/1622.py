# -*- coding: utf8 -*-
import os
import sys

MSG_BAD_MAGICIAN	= "Bad magician!";
MSG_BAD_VOLUNTEER	= "Volunteer cheated!";
MAX_ROW				= 4;
MAX_COL				= 4;

if __name__ == "__main__":
	#input = open("a-sample.txt", "r")
	input = open("a-small.txt", "r")
 	output = open("output-small.txt", "w")
	
	caseMax = int(input.readline());
	
	for caseCounter in range(caseMax):
		answer = int(input.readline()) - 1;
		
		# Get first answer
		for counter in range(MAX_ROW):
			if(counter == answer):
				nums1 = map(int, input.readline().split());
			else:
				input.readline();
		
		# Get second answer
		answer = int(input.readline()) - 1;
		for counter in range(MAX_ROW):
			if(counter == answer):
				nums2 = map(int, input.readline().split());
			else:
				input.readline();
		
		ans_counter = 0;
		ans = -1;
		# compare two answers
		for num1 in nums1:
			for num2 in nums2:
				if (num1 == num2):
					ans_counter = ans_counter + 1;
					ans = num1;
		
		if (1 == ans_counter):
			strResult = "%d" % ans;
		elif (0 == ans_counter):
			strResult = MSG_BAD_VOLUNTEER;
		else:
			strResult = MSG_BAD_MAGICIAN;
		
		strCase = "Case #%d: " % (caseCounter + 1);
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("Done");