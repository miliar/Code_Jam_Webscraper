#!/usr/bin/env python
# encoding: utf-8


import sys
import os
import copy

def calculateWPS(scoreset):
	wps = [];
	for scores in scoreset:
		count = 0.0
		wins = 0.0
		for s in scores:
			if s == "0":
				count += 1.0
			elif s =="1":
				count += 1.0
				wins += 1.0
				
		if count > 0.0:
			wps.append(wins/count)
		else:
			wps.append(0.0)
	return wps
	

def calculateOWPs(scoreset):
	
	owps = []
	
	for i in range(0,len(scoreset)):
		owps.append(calculateOWP(scoreset,i))
	
	return owps
	

def calculateOWP(scoreset,index):
	newScores = copy.deepcopy(scoreset)
	
	opponents = []
	
	#discard games played against you
	for s in range(0,len(newScores)):
		if newScores[s][index] != ".":
			opponents.append(s)
		newScores[s][index] = "."
		
	#find wps without games played against you
	wpsWithoutMe = calculateWPS(newScores)
	
	
	perc = 0.0
	count = 0.0
	
	for j in opponents:
		count += 1.0
		perc += wpsWithoutMe[j]
		
	if count > 0.0:
		return float(perc/count)
	

def calculateOOWP(scoreset, owps, index):
	
	opponents = []
	
	for s in range(0,len(scoreset)):
		if scoreset[s][index] != ".":
			opponents.append(s)
	count = 0.0
	total = 0.0
	
	for i in opponents:
		count += 1.0
		total += owps[i]
	
	if count > 0.0:
		return float(total/count)
	else:
		return 0.0

def calculateOOWPs(scoreset,owps):
	
	oowps = []
	
	for s in range(0,len(scoreset)):
		oowps.append(calculateOOWP(scoreset,owps,s))
		
	return oowps
				

def processRow(nums):
	wps = calculateWPS(nums)
	
	owps = calculateOWPs(nums)
		
	oowps = calculateOOWPs(nums,owps)
	
	rpi = []
	
	for i in range(0,len(wps)):
		rpi.append(0.25*wps[i] + 0.5*owps[i] + 0.25*oowps[i])
	
	return rpi
	

def main():

	infile = open('A-large.txt','r')
	outfile = open('A-large-answer.txt','w')
	
	num_tests = int(infile.readline())

	for x in range(num_tests):
		teams = int(infile.readline())
		scoreset = []
		for i in range(teams):
			score = infile.readline()
			scorelist = [y for y in score.strip()]
			scoreset.append(scorelist)
		
		answer = processRow(scoreset)

		print "Case #"+str((x+1))+":"
		for k in answer:
			print k
			
		outfile.write("Case #"+str(x+1)+": \n")
		for k in answer:
			outfile.write(str(k)+"\n")

	
	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()

