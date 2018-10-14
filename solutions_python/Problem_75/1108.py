#!/usr/bin/python

#
# Google CodeJam 2011
# Qualification Round
# Problem B: Magicka
# Author: dvolgyes
#

import sys
import os

def annihilation(opplist,prev,c2):
	if opplist!=None:
	    for opp in opplist:
		for p in prev:
			if opp[0]==p and opp[1]==c2: return True
			if opp[0]==c2 and opp[1]==p: return True
	return False

def replacable(trlist,c1,c2):
	if trlist!=None:
	    for tr in trlist:
		if tr[0]==c1 and tr[1]==c2: return tr[2]
		if tr[0]==c2 and tr[1]==c1: return tr[2]
	return ""

def solve(trlist,opplist,input):
#	print("OO",opplist)
	if len(input)<2: return input
	lastC=input[0]
	result=""
	for ptr in range(1,len(input)):
		newC=input[ptr]
		if replacable(trlist,lastC,newC)!="":
			result=result+replacable(trlist,lastC,newC)
			lastC=" "
			continue
		if annihilation(opplist,lastC,newC) or annihilation(opplist,result,newC):
			result=""
			lastC=" "
			continue
		if lastC!=" ": 
			result=result+lastC
			lastC=newC
			continue
		lastC=newC
#	print("res:%s %s" % (result,lastC))
	if lastC!=" ": 
		result=result+lastC
		lastC=newC
	return result


CASES=int(sys.stdin.readline())
for case in range(0,CASES):
	input=sys.stdin.readline().strip().split(" ")
	ptr=0
	I=int(input[ptr])
	ptr=ptr+1
	transform=list()
	if I>0:
		transform=[input[ptr]]
		ptr=ptr+1
	for i in range(1,I):
		transform=transform.append(input[ptr].strip())
		ptr=ptr+1
#	print("TR",transform)

	I=int(input[ptr])
	ptr=ptr+1
	oppose=list()
	if I>0:
		oppose=[input[ptr]]
		ptr=ptr+1
	for i in range(1,I):
		oppose=oppose.append(input[ptr].strip())
		ptr=ptr+1

#	print("OPP",oppose)
	I=int(input[ptr])
	ptr=ptr+1
	cards=(input[ptr].strip())

	result=solve(transform,oppose,cards)

	rstr=""
	for i in range(0,len(result)):
		if len(rstr)>0:
			rstr="%s, %s" % (rstr,result[i])
		else:
			rstr="%s" % (result[i])
	print("Case #%s: [%s]" % (case+1,rstr))
