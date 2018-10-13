#!/usr/bin/python2
import sys

def printSol(res):
	if len(res)==1:
		return res[0]
	elif len(res)==0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"


T = int(sys.stdin.readline().strip())
for i in range(1,T+1):
	vals = []
	for p in range(2):
		row = int(sys.stdin.readline().strip())
		for j in range(1,5):
			if row==j:
				vals.append(sys.stdin.readline().strip().split(' '))
			else:
				sys.stdin.readline()

	res = list(set(vals[0])&set(vals[1]))

	print 'Case #'+str(i)+': '+printSol(res)