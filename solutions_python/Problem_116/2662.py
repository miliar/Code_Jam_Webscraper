#!/usr/bin/env python
import sys
sys.path.append("../")
import fileHandler

##################################################
# Lecture fichier
ifile = fileHandler.Fichier("A-small-attempt1.in")
ofile = fileHandler.Fichier("A-small-attempt1.out")
text = ifile.read()
inputs= text.split('\n')
# Fin lecture
##################################################
X = 'X'
O = 'O'
D = 'Draw'
N = 'Game has not completed'

T = int(inputs[0])
##################################################
def getMatrix(inputs,startIndex):
	mat = [[None for i in range(4)] for j in range (4)]
	for i in range(4):
		for j in range(4):
			mat[i][j] = inputs[startIndex + i][j]
	return mat

def resolve(index,mat):
	global X
	global O
	global D
	global N
	state = 0 # 0 draw , 1 still going
	##################################################
	winner = mat[0][0]
	score = 0
	for i in range(4):
		if(winner != '.'):
			if((winner == O and mat [i][i] == X) or (winner == X and mat [i][i] == O)):
				break;
			if(winner == mat[i][i] or winner == 'T' or mat[i][i] == 'T'):
				score += 1
			if (mat[i][i] == X or mat[i][i] == O):
				winner = mat[i][i]
		if(i==3):
			state = 1
	if(score == 4):
		print(winner+" won in main diagonal !!")
		return winner

	print(state)
	##################################################
	winner = mat[0][3]
	score = 0
	for i in range(4):
		if(winner != '.'):
			if((winner == O and mat [i][3-i] == X) or (winner == X and mat [i][3-i] == O)):
				break;
			if(winner == mat[i][3-i] or winner == 'T' or mat[i][3-i] == 'T'):
				score += 1
			if (mat[i][3-i] == X or mat[i][3-i] == O):
				winner = mat[i][3-i]
		if(i==3):
			state = 1		
	if(score == 4):
		print(winner+" won in second diagonal !!")
		return winner
	print(state)
	##################################################
	for k in range(4):
		winner = mat[k][0]
		score = 0
		for i in range(4):
			if(winner != '.'):
				if((winner == O and mat [k][i] == X) or (winner == X and mat [k][i] == O)):
					break;
				if(winner == mat [k][i] or winner == 'T' or mat [k][i] == 'T'):
					score += 1
				if (mat [k][i] == X or mat [k][i] == O):
					winner = mat [k][i]
			if(i==3):
				state = 1
		if(score == 4):
			print(winner+" won in line "+str(k+1)+" !!")
			return winner
	print(state)
	##################################################
	for k in range(4):
		winner = mat[0][k]
		score = 0
		for i in range(4):
			if(winner != '.'):
				if((winner == O and mat [i][k] == X) or (winner == X and mat [i][k] == O)):
					break;
				if(winner == mat [i][k] or winner == 'T' or mat [i][k] == 'T'):
					score += 1
				if (mat [i][k] == X or mat [i][k] == O):
					winner = mat [i][k]
			if(i==3):
				state = 1
		if(score == 4):
			print(winner+" won in column "+str(k+1)+" !!")
			return winner
	print(state)
	return state

response = ""
for i in range(T):
	print(inputs[1+5*i])
	print(inputs[2+5*i])
	print(inputs[3+5*i])
	print(inputs[4+5*i])
	result = resolve(i,getMatrix(inputs,1+5*i))
	if(result == 0):
		result = D
	if(result == 1):
		result = N
	if(result == O):
		result = O+" won"
	if(result == X):
		result = X+" won"
	response = response + "Case #"+str(i+1)+": "+result+"\n"

ofile.write(response)
