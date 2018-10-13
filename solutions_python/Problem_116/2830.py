#!/usr/bin/env python
# encoding: utf-8
"""
tic_tac.py
Created by Aditya Jitta on 2013-04-13.
Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
"""

import sys
import os

def getResult(tempList,i):
	Nzeros=0
	for l in tempList:
		if 0 in l:
			Nzeros+=1
	result=''
	prefix='Case #'
	resArr=[': X won',': O won',': Game has not completed',': Draw']
	rowScores=[]
	colScores=[0,0,0,0]
	diagScores=[0,0]
	dc=0
	for r in tempList:
		rowScores=rowScores+[sum(r)]
		colScores=[colScores[p]+r[p] for p in range(len(r))]
		diagScores[0]=diagScores[0]+r[dc]
		diagScores[1]=diagScores[1]+r[-1-dc]
		dc+=1
	#print '###'
	#print rowScores
	#print colScores
	#print diagScores
	if len([x for x in rowScores if x in [4,3.5]]) > 0:
		result=prefix+str(i)+resArr[0]
	elif len([x for x in colScores if x in [4,3.5]]) > 0:
		result=prefix+str(i)+resArr[0]
	elif len([x for x in rowScores if x in [-4,-2.5]]) > 0:
		result=prefix+str(i)+resArr[1]
	elif len([x for x in colScores if x in [-4,-2.5]]) > 0:
		result=prefix+str(i)+resArr[1]
	elif len([x for x in diagScores if x in [-4,-2.5]]) >0:
		result=prefix+str(i)+resArr[1]
	elif len([x for x in diagScores if x in [4,3.5]]) > 0:
		result=prefix+str(i)+resArr[0]
	if len(result) == 0:
		if Nzeros > 1:
			result=prefix+str(i)+resArr[2]
		else:
			result=prefix+str(i)+resArr[3]
	return result

def main(args):
	scoreDict={'X':1,'O':-1,'T':0.5,'.':0}
	tempList=[]
	FH1=open(args[0])
	FH2 = open(args[1], 'w+')
	count=0
	rcount=0
	for line in FH1.readlines():
		temp=line.split()
		N=len(temp)
		if count==0:
			numCases=eval(line)
		if count >0 and N>0:
			tempList=tempList+[[scoreDict[k] for k in temp[0]]]
		if count > 0 and N == 0:
			rcount+=1
			outtext=getResult(tempList,rcount)+'\n'
			FH2.write(outtext)
			tempList=[]
		count+=1
	FH1.close()
	FH2.close()

if __name__ == '__main__':
	main(sys.argv[1:])
