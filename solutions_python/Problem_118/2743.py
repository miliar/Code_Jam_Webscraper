#coding:utf-8

import sys
import os
import math


def isSquare(N):
	n = N;
	if N == 1:
		return True;
	for i in range(1,n + 2,2):
		if N > 0:
			N = N - i;
		else:
			return 0 == N;

def Palindrome(N):
	L = str(N);
	if L == L[::-1]:
		return True;
	else:
		return False;

inputFile = open("C-small-attempt0.in","r");
outputFile = open("result.in","wb");

T = int(inputFile.readline());

for i in range(T):
	line = inputFile.readline();
	AB = line.split(" ");
	count = 0
	for x in range(int(AB[0]), int(AB[1]) + 1):
		if isSquare(x) and Palindrome(x):
			temp = math.sqrt(x);
			if(Palindrome(int(temp))):
				count += 1;
				print x;
	outputFile.write("Case #" + str(i + 1) + ": " + str(count) + "\n");





