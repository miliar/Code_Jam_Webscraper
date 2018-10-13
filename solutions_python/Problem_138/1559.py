# -*- coding: utf8 -*-
import os
import sys
def warScore(naomis, kens):
	l = len(naomis);
	score = 0;
	i = 0;
	for t in range(l):
		if (naomis[l-score-i-1] < kens[score]):
			return score;
		if (naomis[l-score-i-1] > kens[l-1-i]):
			score = score + 1;
		else:
			i = i + 1;
	return score;

def dwarScore(naomis, kens):
	l = len(naomis);
	score = 0;
	while(l > 0):
		if (naomis[0] > kens[l-1]):
			return score + l;
		if (naomis[l-1] < kens[0]):
			return score;
		t = 0;
		while(naomis[t] < kens[0]):
			t = t + 1;
		del naomis[t];
		del kens[0];
		score = score + 1;
		l = l - 1;
	
	return score;

if __name__ == "__main__":
	#input = open("d-sample.txt", "r")
	input = open("d-large.txt", "r")
 	output = open("output-large.txt", "w")
	
	caseMax = int(input.readline());
	
	for caseCounter in range(caseMax):
		
		maxBlocks = int(input.readline());
		
		blocksNaomi = map(lambda x:int(float(x) * 100000), input.readline().split());
		blocksKen = map(lambda x:int(float(x) * 100000), input.readline().split());
		
		blocksNaomi.sort();
		blocksKen.sort();
		
		strResult = "%d %d" % (dwarScore(blocksNaomi[:], blocksKen[:]), warScore(blocksNaomi, blocksKen));
		
		strCase = "Case #%d: " % (caseCounter + 1);
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		
	print("Done");