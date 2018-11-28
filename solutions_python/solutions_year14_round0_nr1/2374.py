#!/usr/bin/python

import sys


def solveThingy(firstAnswer, firstArangement, secondAnswer, secondArangement):
	candidates = firstArangement[firstAnswer-1]
	answers = []
	for num in secondArangement[secondAnswer-1]:
		if num in candidates:
			answers += [num]
	
	return answers

f = open("input.txt")
numTests = int(f.readline())
output = ""
for i in range(numTests):
	firstAnswer = int(f.readline())
	firstArangement = []
	for j in range(4):
		line = []
		for num in f.readline().split(' '):
			line += [int(num)]
		firstArangement += [line]
	secondAnswer = int(f.readline())
	secondArangement = []
	for j in range(4):
		line = []
		for num in f.readline().split(' '):
			line += [int(num)]
		secondArangement += [line]

	answers = solveThingy(firstAnswer, firstArangement, secondAnswer, secondArangement)

	if len(answers) == 1:
		output += "Case #" + str(i+1) + ": " + str(answers[0]) + '\n'
	elif len(answers) == 0:
		output +=  "Case #" + str(i+1) + ": Volunteer cheated!" + '\n'
	else:
		output +=  "Case #" + str(i+1) + ": Bad magician!" + '\n'
		
fout = open("output.txt", "w")
fout.write(output)

