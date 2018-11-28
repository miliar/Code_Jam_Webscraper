#!/usr/bin/env python2.6
'''
Created on 03/set/2009

@author: marco
'''
import sys
import re

if __name__ == '__main__':
	mainL=[]
	
	inp = open(sys.argv[1], 'r')
	out = open(sys.argv[2], 'w')
	
	line = inp.readline().split(" ")
	L=int(line[0])
	D=int(line[1])
	N=int(line[2])
	
	for i in range(0,D):
		line = inp.readline().rstrip("\n")
		assert(len(line)==L);
		mainL.append(line)
#		lastDict=mainD
#		for c in line:
#			if(False == lastDict.has_key(c)):
#				lastDict[c]={}
	
	for i in range(0,N):
		counter=0
		line = inp.readline()
		line=line.replace("(","[").replace(")","]").rstrip("\n")
		myregexp=re.compile(line)
		for item in mainL:
			if(myregexp.match(item)!=None):
				counter+=1
		out.write("Case #%d: %d\n"%(i+1,counter))
#		line=line.replace("("," ")
#		line=line.replace(")"," ")
#		lline=line.split()
		

	
	
	pass