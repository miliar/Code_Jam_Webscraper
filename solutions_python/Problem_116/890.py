#! /usr/bin/python

from sys import argv,exit

def check_result(linea):
	if   linea == "XXXX" or linea == "TXXX" or linea == "XTXX" or linea == "XXTX" or linea == "XXXT" :
		return 1
	elif linea == "OOOO" or linea == "TOOO" or linea == "OTOO" or linea == "OOTO" or linea == "OOOT":
		return 2
	return 0

def analizar_caso(caso):
	for linea in caso:
		res = check_result(linea)
		if res :
			if res == 1:
				return "X won"
			else:
				return "O won"

	for i in range(4):
		col = caso[0][i] + caso[1][i] + caso[2][i] + caso[3][i]

		res = check_result(col)
		if res :
			if res == 1:
				return "X won"
			else:
				return "O won"

	diag = caso[0][0] + caso[1][1] + caso[2][2] + caso[3][3]

	res = check_result(diag)
	if res :
		if res == 1:
			return "X won"
		else:
			return "O won"

	diag = caso[0][3] + caso[1][2] + caso[2][1] + caso[3][0]

	res = check_result(diag)
	if res :
		if res == 1:
			return "X won"
		else:
			return "O won"

	if [a for a in "".join(caso) if a == '.']:
		return "Game has not completed"
	else:
		return "Draw"


if len(argv) != 3:
	print "Usage: prog <filein> <fileout>"
	exit(0)

filein = open(argv[1],"r")
fileout = open(argv[2],"w")

lines = filein.read().split("\n")
ncases = int(lines[0])

x=1
for i in range(1,ncases+1):
	fileout.write("Case #" + str(i) + ": ")
	fileout.write(analizar_caso(lines[x:x+4]) + "\n")
	x = x + 5
