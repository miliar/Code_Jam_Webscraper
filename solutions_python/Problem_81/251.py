#!/usr/bin/env python
import math
import sys
import os
from os import system

def WP(team,N):
	wplist = []
	sumlist = []
	onelist = []
	owpboard = []
	i = 0
	for t in team:
		sum = 0
		one = 0
		for n in t: 
			if n is ".":
				continue
			elif n is "1":
				sum += 1
				one += 1
			elif n is "0":
				sum += 1
		sumlist.append(sum)
		onelist.append(one)
		wplist.append(float(one)/sum)

		owpboard.append([])
		for n in t:
			if n is ".":
				owpboard[i].append(".")
			elif n is "1":
				owpboard[i].append(float(onelist[i]-1)/(sumlist[i]-1))
			elif n is "0":
				owpboard[i].append(float(onelist[i])/(sumlist[i]-1))
		i += 1

	owplist = []
	sumlist2 = []
	for i in range(N):
		owplist.append(0.0)
		sumlist2.append(0)
	for i in range(N):
		for j in range(N):
			if owpboard[i][j] is ".":
				continue
			owplist[j] += owpboard[i][j]
			sumlist2[j] += 1
	for j in range(N):
		owplist[j] = float(owplist[j])/sumlist2[j]

	oowplist = []
	for t in team:
		sum = 0
		score = 0.0
		i = 0
		for n in t:
			if n is ".":
				i += 1
				continue
			sum += 1
			score += float(owplist[i])
			i += 1
			#print sum, score
		oowplist.append(score/sum)

	#print wplist
	#print owpboard
	#print owplist
	#print "!!"
	#print oowplist
	return wplist, owplist, oowplist

	


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	N = int(l[0])
	team = []
	for j in range(N):
		team.append([])
		tokens = fp.readline()
		for k in range(N):
			team[j].append(tokens[k])
	
	#print team

	wplist, owplist, oowplist = WP(team,N)
	rpi = []
	for j in range(N):
		score = 0.25*wplist[j] + 0.5*owplist[j] + 0.25*oowplist[j]
		rpi.append(score)
	

	fout.write('Case #%d:\n'%((i+1)))
	for j in range(N):
		fout.write('%.8f\n'%(rpi[j]))
