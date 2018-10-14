#!/usr/bin/python

import sys

def average(values):
	return sum(values, 0.0) / len(values)

fin = open ('A-large.in', 'r')
fout = open('A-large.out', 'w')

casenum = int(fin.readline())

for i in range(casenum):
	print "Case #{}: ".format(i+1)
	fout.write("Case #{}: \n".format(i+1))
	teamCount = int(fin.readline())
	scoreBoard = []
	wp = []
	owp = []
	for j in range(teamCount):
		scoreBoard.append(list(fin.readline().rstrip()))
		wp.append(float(scoreBoard[j].count('1')) / (scoreBoard[j].count('1') + scoreBoard[j].count('0')))

	for j in range(teamCount):
		owpT = []
		for k in range(teamCount):
			if(j != k) and scoreBoard[k][j] != '.':
				owpT.append(float(scoreBoard[k].count('1') - float(scoreBoard[k][j])) / (scoreBoard[k].count('1') + scoreBoard[k].count('0') - 1))
		owp.append(owpT)

	for j in range(teamCount):
		rpi =  0.25 * wp[j]
		rpi += 0.5 * average(owp[j])
		oowp = []
		for k in range(teamCount):
			if scoreBoard[j][k] != '.':
				oowp.append(average(owp[k]))
		rpi += 0.25 * average(oowp)
		print rpi
		fout.write("{}\n".format(rpi))
	

fin.close()
fout.close()
