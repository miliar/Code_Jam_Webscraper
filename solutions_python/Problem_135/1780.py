#!/usr/bin/python
import sys

f = open("A-small-attempt0.in")
cases = int(f.readline())
for j in range(cases):
	line1 = int(f.readline())-1
	matrix1 = []
	for i in range(4):
		matrix1.append(list(map(int,f.readline().split(" "))))
	line2 = int(f.readline())-1
	matrix2 = []
	for i in range(4):
		matrix2.append(list(map(int,f.readline().split(" "))))

	finalList = list(set(matrix1[line1]).intersection(set(matrix2[line2])))
	if len(finalList)==0:
		print "Case #"+str(j+1)+": Volunteer cheated!"
	elif len(finalList)==1:
		print "Case #"+str(j+1)+": " + str(finalList[0])
	else:
		print "Case #"+str(j+1)+": Bad magician!"
