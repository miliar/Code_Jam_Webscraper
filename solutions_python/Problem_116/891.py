# Alien Language
# Open a file
import re

infile = open("A-large.in","r")
outfile = open("output.txt","w")
lines = infile.readlines()

params = lines[0].rstrip()

for i in range(0,int(params)):
	game = []
	winX = 0
	winO = 0
	countD = 0
	for j in range(0,4):
		game.append(list(lines[1+i*5+j].rstrip()))
		countD = countD+game[j].count('.')

	# check which person has won
	for j in range(0,4):
		if(game[j].count('O') == 0 and game[j].count('.') == 0):
			winX = 1
			break
		if(game[j].count('X') == 0 and game[j].count('.') == 0):
			winO = 1
			break
	
	gameT = [[r[col] for r in game] for col in range(len(game[0]))]  
	for j in range(0,4):
		if(gameT[j].count('O') == 0 and gameT[j].count('.') == 0):
			winX = 1
			break
		if(gameT[j].count('X') == 0 and gameT[j].count('.') == 0):
			winO = 1
			break

	diag = [[game[0][0],game[1][1],game[2][2],game[3][3]], [game[0][3],game[1][2],game[2][1],game[3][0]]]
	if(diag[0].count('O') == 0 and diag[0].count('.') == 0):
		winX = 1
	if(diag[0].count('X') == 0 and diag[0].count('.') == 0):
		winO = 1
	if(diag[1].count('X') == 0 and diag[1].count('.') == 0):
		winO = 1
	if(diag[1].count('O') == 0 and diag[1].count('.') == 0):
		winX = 1

	# output result to file
	if(winX==0 and winO==0 and countD==0):	
		outfile.writelines("Case #"+str(i+1)+": Draw\n")
	elif(winX==1 and winO==0):
		outfile.writelines("Case #"+str(i+1)+": X won\n")
	elif(winX==0 and winO==1):
		outfile.writelines("Case #"+str(i+1)+": O won\n")
	elif(winX==0 and winO==0 and countD!=0):
		outfile.writelines("Case #"+str(i+1)+": Game has not completed\n")

infile.close()
outfile.close()