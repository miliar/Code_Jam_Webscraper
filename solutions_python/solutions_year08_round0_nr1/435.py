#!/usr/bin/python

import sys

def ReadInput():
	f=sys.stdin.readlines()
	data={}
	N=int(f[0])
	i=1
	for x in range(0,N):
		S=int(f[i])
		SE = []
		i=i+1
		for y in range(0,S):			
			SE.append(f[i].strip())
			i=i+1
		Q = int(f[i])
		QE = []
		i=i+1
		for z in range(0,Q):
			QE.append(f[i].strip())
			i=i+1
		data[x]=(SE,QE)
	return data
	
def ProcessSearch(case, SE, QE):
	switch=-1
	se=None
	i=0
	while i<len(QE):
		place={}
		for x in SE:
			place[x]=2000
		for x in range(i,len(QE)):
			if place[QE[x]] == 2000:
				place[QE[x]] = x
		place2={}
		for x in place.iteritems():
			place2[x[1]]=x[0]
		i=max(place2)
		if(i > len(QE)):
			return switch+1
		
		
		while (QE[i] == se):
			del(place2[i])
			i = max(place2)
			if(i > len(QE)):
				return switch+1
		se = QE[i]
		switch+=1
		
	if switch < 0:
		return 0
	return switch
	

		
if __name__ == "__main__":
	data = ReadInput()
	for x in range(0,len(data)):
		print "Case #%d: %s" %(x+1,(ProcessSearch(x, data[x][0], data[x][1])))
		
		
		