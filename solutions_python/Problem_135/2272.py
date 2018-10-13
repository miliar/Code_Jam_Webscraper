# -*-coding:utf-8 -*

import sys
from os import system

def solve(r1, b1, r2, b2):
	cpt = int(0)
	r1 -=1
	r2 -=1
	for x in range(4):
			if b1[r1][x] in b2[r2]:
				cpt += 1
				carte = b1[r1][x]
	if cpt == 1:
		return str(carte)
	if cpt > 1:
		return 'Bad magician!'
	return 'Volunteer cheated!'


entree = open("./A-small-attempt0.in", "r")
sortie = open("./A-small-attempt0.out", "w")
numcases = int(entree.readline())
for casenum in range(1,numcases+1):
	board1 = []
	board2 = []
	rep1 = int(entree.readline())
	for i in range(4):
		board1.append(entree.readline().strip())
		board1[i] = board1[i].split()
	rep2 = int(entree.readline())
	for j in range(4):
		board2.append(entree.readline().strip())
		board2[j] = board2[j].split()
	s = str("Case #" + repr(casenum) + ": " + solve(rep1, board1, rep2, board2)+'\n')
	sortie.write(s)
entree.close()
sortie.close()
