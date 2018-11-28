#!/usr/bin/python

import sys

games=[]

def wp(team):
	result=0
	total=0
	for charac in games[team]:
		if charac=="1":
			result=result+1
			total=total+1
		if charac=="0":
			total=total+1
	return float(result)/float(total)

def wpExcept(team,excep):
	result=0
	total=0
	element=0;
	for charac in games[team]:
		if element==excep:
			element=element+1
			continue
		if charac=="1":
			result=result+1
			total=total+1
		if charac=="0":
			total=total+1
		element=element+1
	return float(result)/float(total)

def owp(team):
	average=float(0)
	oponents=0	

	for myteam in range(len(games)):
		if myteam==team:
			continue
		if games[team][myteam]!='.':
			average=average+wpExcept(myteam,team)
			oponents=oponents+1
	divide=float(oponents)
	average=average/divide
	return average

def oowp(team):
	average=float(0)
	oponents=0
	for myteam in range(len(games)):
		if myteam==team:
			continue
		if games[team][myteam]!='.':
			average=average+owp(myteam)
			oponents=oponents+1
	divide=float(oponents)
	average=average/divide
	return average

def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***
	results=[]	
	myWP=float()
	myOWP=float()
	myOOWP=float()

	for team in range(len(games)):
		myWP=wp(team)
		myOWP=owp(team)		
		myOOWP=oowp(team)
		#print "TEAM "+str(team)+" WP= "+str(myWP)+" OWP= "+str(myOWP)+" OOWP= "+str(myOOWP)
		results.append((0.25*myWP)+(0.5*myOWP)+(0.25*myOOWP))

	# *** END CODE PROCESSING CASE ***
	return results 

def readCase(case):
	global games
	solution=[]	

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()

	teams=int(caseInput)

	for itr in range(teams):
		games.append((sys.stdin.readline()).split()[0])
		
	# *** END CODE READING CASE ***

	solution=processCase(case)
	print "Case #"+str(case)+": "
	for itr in range(teams):
		print str(solution[itr])

	games=[]

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

