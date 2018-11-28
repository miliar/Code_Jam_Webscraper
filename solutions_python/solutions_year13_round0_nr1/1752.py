#!/usr/bin/python
# -*- coding: utf-8 -*-

def ligneWon(plateau, ligne, joueur):
	for j in range(4):
		if (plateau[ligne][j] != joueur) and (plateau[ligne][j] != 'T'):
			return False
	return True

def colonneWon(plateau, colonne, joueur):
	for j in range(4):
		if (plateau[j][colonne] != joueur) and (plateau[j][colonne] != 'T'):
			return False
	return True

def firstDiagonaleWon(plateau, joueur):
	for j in range(4):
		if (plateau[j][j] != joueur) and (plateau[j][j] != 'T'):
			return False
	return True

def secondDiagonaleWon(plateau,joueur):
	for j in range(4):
		if (plateau[j][3-j] != joueur) and (plateau[j][3-j] != 'T'):
			return False
	return True	

def gameIsDraw(plateau):
	for ligne in plateau:
		if '.' in ligne:
			return False
	return True

inputFile = open("A-large.in","r")
solution = open("A-large.out","w")

T = int(inputFile.readline().split("\n")[0])

for i in range(T):
	plateau = []
	for j in range(4):
		ligne = inputFile.readline()
		liste = []
		liste.append(ligne[0])
		liste.append(ligne[1])
		liste.append(ligne[2])
		liste.append(ligne[3])
		plateau.append(liste)

	xWon = firstDiagonaleWon(plateau,'X') or secondDiagonaleWon(plateau,'X')
	oWon = firstDiagonaleWon(plateau,'O') or secondDiagonaleWon(plateau,'O')
	draw = gameIsDraw(plateau)

	for j in range(4):
		if ligneWon(plateau, j, 'X'):
			xWon = True
		if ligneWon(plateau, j, 'O'):
			oWon = True
		if colonneWon(plateau, j, 'X'):
			xWon = True
		if colonneWon(plateau, j, 'O'):
			oWon = True

	reponse = "Game has not completed"
	if draw:
		reponse = "Draw"

	if xWon:
		reponse = "X won"
	if oWon:
		reponse = "O won"
	if xWon and oWon:
		print "probleme"

	inputFile.readline()
	solution.write("Case #"+str(i+1)+": "+reponse+"\n")
