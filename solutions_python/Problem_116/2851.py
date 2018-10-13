#!/bin/python3

import sys, re, string

line=sys.stdin.readline()
tX=str.maketrans("T", "X")
tO=str.maketrans("T", "O")
for case in range(0, int(line)):
	xFlag=False
	oFlag=False
	compFlag=True
	line=[]
	line.append(sys.stdin.readline()[:-1])
	line.append(sys.stdin.readline()[:-1])
	line.append(sys.stdin.readline()[:-1])
	line.append(sys.stdin.readline()[:-1])
	sys.stdin.readline()
	for i in range(0, 4):
		if "." in line[i]:
			compFlag=False
		if line[i].translate(tX) == "XXXX":
			xFlag=True
		if line[i].translate(tO) == "OOOO":
			oFLag=True
	if "".join(list(line[i])[i] for i in range(0,4)).translate(tX) == "XXXX":
		xFlag=True
	if "".join(list(line[i])[3-i] for i in range(0,4)).translate(tX) == "XXXX":
		xFlag=True
	if "".join(list(line[i])[i] for i in range(0,4)).translate(tO) == "OOOO":
		oFlag=True
	if "".join(list(line[i])[3-i] for i in range(0,4)).translate(tO) == "OOOO":
		oFlag=True
	for i in zip(line[0],line[1],line[2],line[3]):
		if "".join(x for x in i).translate(tX) == "XXXX":
			xFlag=True
		if "".join(x for x in i).translate(tO) == "OOOO":
			oFlag=True
	if xFlag and oFlag:
		print("Case #"+str(case+1)+": Draw")
	elif xFlag:
		print("Case #"+str(case+1)+": X won")
	elif oFlag:
		print("Case #"+str(case+1)+": O won")
	else:
		if compFlag:
			print("Case #"+str(case+1)+": Draw")
		else:
			print("Case #"+str(case+1)+": Game has not completed")
