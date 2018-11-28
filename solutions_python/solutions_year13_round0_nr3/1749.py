# -*- coding: utf8 -*-
import os
import sys

import math

def isPalindrome(num):
	candy = str(num);
	maxIdx = len(candy);
	if(1 == num or 2 == num):
		return True;
	idx = 0;
	
	while(idx < maxIdx):
		#print("idx : %d / len(candy) : %d" % (idx, len(candy)));
		if(candy[idx] != candy[len(candy) - idx - 1]):
			break;
		idx = idx + 1;
		
	if (idx >= maxIdx):
		#print("Candy : %d / (%d)" % (num, num**.5));
		if ((num**.5 % 1) == 0):
			return isPalindrome(int(num**.5));
		else:
			#print("Return true");
			return True;
	#print("Sorry, %d is not palindrome" % num);
	return False;

if __name__ == "__main__":
	#input = open("c-sample.txt", "r")
	input = open("C-small.in", "r")
	output = open("output-small.txt", "w")
	
	maxCase = int(input.readline())
	
	for caseCounter in range(maxCase):
		nums = list(map(int, input.readline().split()))
		minRange = nums[0];
		maxRange = nums[1];
		
		newMin = int(math.ceil(minRange**.5));
		newMax = int(math.ceil(maxRange**.5)) + 1;
		
		#print ("%d, %d" % (newMin, newMax));
		
		foundCounter = 0;
		
		for num_o in range(newMin, newMax):
			num = num_o * num_o;
			if(num < minRange):
				continue;
			if(num > maxRange):
				break;
			#print("%d (%d ~ %d)" % (num, minRange, maxRange));
			if (True == isPalindrome(num)):
				foundCounter = foundCounter + 1;
				#print("found : %s (%d)" % (num, num_o));
		
		strResult = str(foundCounter);
		
		strCase = "Case #%d: " % (caseCounter + 1);
		#strResult = "%d mm" % maxHeight;
		
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("done")