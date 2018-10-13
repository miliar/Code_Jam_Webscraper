#!/usr/bin/python3

import sys

def readTest(inputfile):
	row1 = int(inputfile.readline())
	arrangement1 = []
	for i in range(4):
		arrangement1.append([int(x) for x in inputfile.readline().split()])

	row2 = int(inputfile.readline())

	arrangement2 = []
	for i in range(4):
		arrangement2.append([int(x) for x in inputfile.readline().split()])

	return row1,row2,arrangement1,arrangement2

def evaluate(row1,row2,arr1,arr2):
	first = arr1[row1 - 1]
	snd = arr2[row2 - 1]

	result = [x for x in first if x in snd]

	return result

if (len(sys.argv) == 2):
	text = open(sys.argv[1],'r')

	testCount = int(text.readline())
	
	for i in range(testCount):
		row1,row2,arr1,arr2 = readTest(text)
		result = evaluate(row1,row2,arr1,arr2)
		if (len(result) == 1):
			print("Case #{}: {}".format(i + 1, result[0]))
		elif (len(result) == 0):
			print("Case #{}: Volunteer cheated!".format(i+1))
		else:
			print("Case #{}: Bad magician!".format(i+1))
