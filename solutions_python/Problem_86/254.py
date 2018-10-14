#!/usr/bin/python

import sys

def processCase(lowest,highest,list):
	# *** BEGIN CODE PROCESSING CASE ***
	
	frecuencies=[]
	for music in list:
		musicset=set()
	
		# frecuencias / alguna de las mias es divisible entre musica	
		multiplier=1
		while (multiplier*music)<=highest:
			if (multiplier*music)>=lowest:
				musicset.add(multiplier*music)
			multiplier=multiplier+1

		# frecuencias / musica es divisible entre alguna de las mias

		if music>=lowest:
			maxtotest=min(music,highest)

			for mysmall in range(lowest,maxtotest+1):
				if ((music%mysmall)==0) :
					musicset.add(mysmall)

		frecuencies.append(musicset)

	commonfrecuencies=frecuencies[0]
	frecuencies.pop(0)
	for nset in frecuencies:
		commonfrecuencies=commonfrecuencies.intersection(nset)

	if len(commonfrecuencies)==0:
		return -1
	else:
		# sort
		freclist=[]
		for f in commonfrecuencies:
			freclist.append(f)
		freclist.sort()
		#print freclist
		return freclist[0]

	# *** END CODE PROCESSING CASE ***

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
	tokens=caseInput.split()
	lowest=int(tokens[1])
	highest=int(tokens[2])
	caseInput=sys.stdin.readline()
	tokens=caseInput.split()
	list=[]	
	for itr in tokens:
		list.append(int(itr)) 
		
	# *** END CODE READING CASE ***

	solution=processCase(lowest,highest,list)
	if solution==-1:
		print "Case #"+str(case)+": NO"
	else:
		print "Case #"+str(case)+": "+str(solution)

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

