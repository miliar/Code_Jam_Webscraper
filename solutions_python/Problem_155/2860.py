# -*- coding: utf8 -*-
import os
import sys


if __name__ == "__main__":
	#input = open("a-sample.txt", "r")
	input = open("A-large.in", "r")
 	output = open("output-large.txt", "w")
	
	caseMax = int(input.readline());
	
	for caseCounter in range(caseMax):
		t = input.readline().split();
		maxLevel = int(t[0]);
		peoples = [];
		cur = 0;
		needs = 0;
		for levelCounter in range(maxLevel + 1):
			ppl = int(t[1][levelCounter])
			if 0 < ppl and levelCounter > cur:
				needs = needs + levelCounter - cur;
				cur = levelCounter;
			cur = cur + ppl;
		
		strResult = "Case #%d: %d\n" % ((caseCounter + 1), needs);
		print(strResult);
		output.write(strResult);
		
	print("Done");