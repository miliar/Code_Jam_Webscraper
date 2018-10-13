#!/usr/bin/env python2.6

'''
Created on 03/set/2009

@author: marco
'''
import sys


def singleRec(origString,findString):
	
	retval=0
	lastRes=0
	Found=False
	for stringPtr in range(len(origString)-len(findString)+1):
		if(len(findString)>1 and Found and origString[stringPtr]==findString[1]):
			Found=False
			
		if origString[stringPtr]==findString[0]:
			if(len(findString)>1):
				if(not Found):
					lastRes=singleRec(origString[stringPtr+1:], findString[1:])
					Found=True
				retval+=lastRes
			else:
				retval+=1
	return retval
	
	
if __name__ == '__main__':

	myString="welcome to code jam"
	
	inp = open(sys.argv[1], 'r')
	out = open(sys.argv[2], 'w')
	
	line = inp.readline().rstrip("\n")
	N=int(line)
	
	for i in range(0,N):
		#line = inp.readline().rstrip("\n").lower()
		line = inp.readline().rstrip("\n")
		oline=line
		
		tot_sum=singleRec(line, myString)
		
		res=("000%d"%tot_sum)[-4:]
		out.write("Case #%d: %s\n"%(i+1,res))

