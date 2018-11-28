#!/usr/bin/env python2.6
'''
Created on 03/set/2009

@author: marco
'''
import sys
import re


class treeElem:
	def __init__(self,my_weight):
		self.weight=my_weight
		self.hasFeature=False
		self.Rlines=1

def readTree(infile):
	#Quick and dirty, I hope it's enough well formatted
	lines=infile.readline().rstrip("\n").lstrip(" ").replace("  "," ").split(" ")
	assert(lines[0][0]=="(");
	lines[0]=lines[0][1:]
	if(lines[0]==''):
		lines=lines[1:]
	if lines[-1][-1]==")":
		lines[-1]=lines[-1][:-1]
		extraClose=0
		while(len(lines[-1])>0 and lines[-1][-1]==")"):
			extraClose+=1
			lines[-1]=lines[-1][:-1]
		if(lines[-1]==''):
			lines=lines[:-1]
		assert(len(lines)==1)
		retval=treeElem(float(lines[0]))
		retval.extraClose=extraClose
		return retval
	else:
		retval=treeElem(float(lines[0]))
		if(len(lines)==2):
			retval.hasFeature=True;
			retval.feature=lines[1]
		else:
			assert(False)
		tree1=readTree(infile)
		retval.Rlines+=tree1.Rlines
		assert(tree1.extraClose==0)
		tree2=readTree(infile)
		retval.Rlines+=tree2.Rlines
		retval.extraClose=tree2.extraClose
		retval.tree1=tree1
		retval.tree2=tree2
		if(retval.extraClose>0):
			retval.extraClose-=1
		else:
			lines=infile.readline().rstrip("\n").lstrip(" ").replace("  "," ").split(" ")
			assert(len(lines)==1)
			assert(lines[0][0]==")")
			
	
	return retval

if __name__ == '__main__':
	mainL=[]
	
	inp = open(sys.argv[1], 'r')
	out = open(sys.argv[2], 'w')
	
	line = inp.readline().rstrip("\n")
	N=int(line)
	for i in range(N):
		out.write("Case #%d:\n"%(i+1))
		line = inp.readline().rstrip("\n")
		L=int(line)
		root=readTree(inp)
		line = inp.readline().rstrip("\n")
		a=int(line)
		for animal in range(a):
			myAn=inp.readline().rstrip("\n").lstrip(" ").replace("  "," ").split(" ")
			myAnE=int(myAn[1])
			myAn=myAn[2:]
			anD=set()
			for elem in myAn:
				anD.add(elem)
			assert(len(anD)==myAnE)
			
			cT=root;
			cP=1
			while(cT.hasFeature):
				cP*=cT.weight
				if(cT.feature in anD):
					cT=cT.tree1
				else:
					cT=cT.tree2
			cP*=cT.weight
			res=("%f0000000"%cP)[:9]
			out.write("%s\n"%(res))
	
	

