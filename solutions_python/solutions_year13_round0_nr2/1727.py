#coding:utf-8

import sys
import os

def CompareArray(a):
	current = a[0];
	for i in range(1, len(a)):
		if a[i] != current:
			return False;
	return True;

def MatrixProcessing(a):
	row = [];
	col = [];
	for i in range(len(a)):
		if CompareArray(a[i]) and a[i][0] == 1:
			row.append(i);
	for j in range(len(a[0])):
		temp = [];
		for i in range(len(a)):
			temp.append(a[i][j]);
		if CompareArray(temp) and temp[0] == 1:
			col.append(j);

	return [row, col];

def PosisRight(a, Pos):
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] == 1 and ((i not in Pos[0]) and (j not in Pos[1])):
				return "NO";

	return "YES";


inputFile = open("B-small-attempt0.in","r");
outputFile = open("result.in","wb");

T = int(inputFile.readline());

for i in range(T):
	line = inputFile.readline();
	NM = line.split(" ");
	strLawn = [];
	Lawn = [];
	for k in range(int(NM[0])):
		strLawn.append((inputFile.readline()).split(" "));
	for x in range(int(NM[0])):
		Lawn.append([]);
		#print x;
		#print Lawn;
		for y in range(int(NM[1])):
			Lawn[x].append(int(strLawn[x][y]));

	Pos = MatrixProcessing(Lawn);

	outputFile.write("Case #" + str(i + 1) + ": " + PosisRight(Lawn, Pos) + "\n");
	print PosisRight(Lawn, Pos);

	#print Lawn;