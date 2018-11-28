#!/usr/bin/python
import sys

def aux(naomi,ken):
	for j in range(len(ken)):
		if naomi[0]<ken[j]:
			del ken[j]
			del naomi[0]
			return 0
	del ken[0]
	del naomi[0]
	return 1

def calcWar(naomi,ken):
	points = 0
	for i in range(len(naomi)):
		points += aux(naomi,ken)
	return points 

def calcDeceitfulWar(naomi, ken):
	points = 0
	for i in range(len(naomi)-1,-1,-1):
		for j in range(len(ken)-1,-1,-1):
			if naomi[i]>ken[j]:
				points += 1
				del naomi[i]
				del ken[j]
				break

	return points

f = open("D-large.in")
cases = int(f.readline())
for j in range(cases):
	blocks = int(f.readline())

	naomiBlocks = list(map(float,f.readline().split(" ")))
	kenBlocks = list(map(float,f.readline().split(" ")))
	naomiBlocks.sort()
	kenBlocks.sort()
	
	warPoints = calcWar(naomiBlocks[:],kenBlocks[:])
	deceitfulPoints = calcDeceitfulWar(naomiBlocks[:],kenBlocks[:])

	print "Case #"+str(j+1)+": " + str(deceitfulPoints) + " " + str(warPoints)