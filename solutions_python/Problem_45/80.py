#!/usr/bin/env python2.6
'''
Created on 03/set/2009

@author: marco
'''
import sys
import re

class prig:
	def __init__(self,myID,P):
		self.P=P
		self.myID=myID
		self.Sx=myID-1
		self.Dx=P-myID
	def __cmp__(self,other):
		selfP=self.Sx+self.Dx
		otherP=other.Sx+other.Dx
		if(cmp(selfP,otherP)!=0):
			return cmp(selfP,otherP)
		else:
			if(self.Sx<self.Dx):
				minP=self.Sx
			else:
				minP=self.Dx
			if(other.Sx<other.Dx):
				minO=other.Sx
			else:
				minO=other.Dx
			return -1*cmp(minP,minO)
	def update(self,Rel):
		if(self.myID<Rel):
			if(self.Dx>(Rel-self.myID-1)):
				self.Dx=(Rel-self.myID-1)

		else:
			if(self.Sx>(self.myID-Rel-1)):
				self.Sx=(self.myID-Rel-1)
	def reset(self):
		self.Sx=self.myID-1
		self.Dx=self.P-self.myID

			
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]
	

if __name__ == '__main__':
	mainL=[]
	
	inp = open(sys.argv[1], 'r')
	out = open(sys.argv[2], 'w')
	
	line = inp.readline().rstrip("\n")
	T=int(line)
	for test_id in range(T):
		print "Test casde %d/%d"%(test_id+1,T)
		out.write("Case #%d: "%(test_id+1))
		
		line = inp.readline().split(" ")
		P=int(line[0])
		Q=int(line[1])
		line = inp.readline().split(" ")
		assert(len(line)==Q)
		
		myP=[]
		for prigID in line:
			myP.append(prig(int(prigID),P))
			
		
#		myCost=0
#		while(len(myP)>0):
#			myP.sort()
#			myCost+=myP[0].Dx+myP[0].Sx
#			exitP=myP[0].myID
##			print "exiting %d, cost %d\n"%(exitP,myP[0].Dx+myP[0].Sx)
#			myP.pop(0)
#			for restP in myP:
#				restP.update(exitP)

		minT=10000000
		for per in all_perms(myP):
			for toR in per:
				toR.reset() 
			cost=0
			while(len(per)>0):
				cost+=per[0].Dx+per[0].Sx
				exitP=per[0].myID
				per.pop(0)
				for restP in per:
					restP.update(exitP)
			if(cost<minT):
				minT=cost
				
		myCost=minT


		
		out.write("%d\n"%myCost)
			
	
	

