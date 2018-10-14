#!/usr/bin/python
import sys

file_arg = sys.argv[1]
f = open(file_arg, 'r')
string = ""
for i in range(int(f.readline())):
	firstIndex = int(f.readline())-1
	firstList = [];
	for j in range(int(4)):
		if j == firstIndex:
			firstList = [int(k) for k in f.readline().split()]
		else:
			f.readline()
	secondIndex = int(f.readline())-1
	secondList = [];
	for j in range(int(4)):
		if j == secondIndex:
			secondList = [int(k) for k in f.readline().split()]
		else:
			f.readline()
	intersect = list(set(firstList).intersection(secondList))
	intersectLength = len(intersect)
	text = ""
	if(intersectLength == 1):
		text = str(intersect[0])
	if(intersectLength == 0):
		text = "Volunteer cheated!"
	if(intersectLength > 1):
		text = "Bad magician!"
	string+="Case #" + str(i + 1) + ": " + text + "\n"

text_file = open("output.out", "w")
text_file.write(string)
text_file.close()