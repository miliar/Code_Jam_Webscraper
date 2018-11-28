#!/usr/bin/python
import fileinput
import sys
import numpy
import copy
import math

def prt(txt):
	sys.stdout.write(txt);



def main():
	count = int(raw_input())

	for c in range(0,count):
		prt("Case #" + str(c + 1)+": ")

		N = int(raw_input())

		pattern = []
		strs = []

		valid = True;
		for i in range(0,N):
			letter = -1
			char = '\0'
			string = raw_input();

			strs.append([])

			for j in range(0,len(string)):
				if(string[j] != char):
					char = string[j]
					letter += 1;
					strs[i].append(1)
					if i == 0:
						pattern.append(char)

					elif len(pattern) == letter or pattern[letter] != char:
						#prt("found "+char +" expecting "+pattern[letter])
						valid = False
						break
				else:
					strs[i][letter] += 1;
			if(len(strs[i]) != len(pattern)):
				valid = False

			if not valid:
				break
		if not valid:
			prt("Fegla Won\n");
			continue

		letters = len(pattern);

		moveCount = 0

		for j in range(0,letters):
			mean = 0
			for i in range(0,N):
				mean += strs[i][j]
			mean /= N;
			#round to the nearest number
			mean = int(math.floor(mean + 0.5))
			for i in range(0,N):
				moveCount += abs(strs[i][j] - mean)

		prt(str(int(moveCount))+"\n")
				








main()