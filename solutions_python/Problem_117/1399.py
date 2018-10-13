# -*- coding: utf8 -*-
import os
import sys

class Candy:
	x = 0;
	y = 0;
	val = 100;

if __name__ == "__main__":
	#input = open("b-sample.txt", "r")
	input = open("B-large.in", "r")
	output = open("output-large.txt", "w")
	
	maxCase = int(input.readline())
	
	for caseCounter in range(maxCase):
		nums = list(map(int, input.readline().split()))
		maxRow = nums[0];
		maxCol = nums[1];
		
		lawn = [];
		
		maxHeight = 0;
		minHeight = 100;
		
		for loop in range(maxRow):
			nums = list(map(int, input.readline().split()));
			
			x = 0;
			for num in nums:
				item = Candy();
				item.x = x;
				item.y = loop;
				item.val = num;
				x = x + 1;
				
				lawn.append(item);
			
		
		lawn.sort(key=lambda x: x.val, reverse=True);
		
		required_x = [];
		for loop in range(maxCol):
			required_x.append(0);
		
		required_y = [];
		for loop in range(maxRow):
			required_y.append(0);
		
		strResult = "YES";
		for item in lawn:
			#print("%d (%d, %d) / req_x : %d, req_y : %d" % (item.val, item.x, item.y, required_x[item.x], required_y[item.y]));
			if required_x[item.x] > item.val and required_y[item.y] > item.val:
				strResult = "NO";
				break;
			if required_x[item.x] < item.val:
				required_x[item.x] = item.val;
			if required_y[item.y] < item.val:
				required_y[item.y] = item.val;
		
		
		strCase = "Case #%d: " % (caseCounter + 1);
		#strResult = "%d mm" % maxHeight;
		
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("done")