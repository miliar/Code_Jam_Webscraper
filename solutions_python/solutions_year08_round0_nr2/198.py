#! /usr/bin/python

from math import *
from sys import *

ARRIVE_A=0
ARRIVE_B=1
DEPART_A=2
DEPART_B=3

def solve(events):
	ret_A=0
	ret_B=0
	tA=0
	tB=0
	
	for e in events:
		if e[1]==ARRIVE_A:
			tA+=1
		elif e[1]==ARRIVE_B:
			tB+=1
		elif e[1]==DEPART_A:
			if tA:
				tA-=1
			else:
				ret_A+=1
		elif e[1]==DEPART_B:
			if tB:
				tB-=1
			else:
				ret_B+=1
	return (ret_A, ret_B)
	
def tomin(tm):
	return int(tm[0])*60+int(tm[1])
	
if __name__=='__main__':
	N=int(stdin.readline())
	for case in xrange(1,N+1):
		T=int(stdin.readline())
		(NA,NB)=map(int, stdin.readline().split())
		events=[]
		for i in xrange(NA):
			line=stdin.readline()
			start,end=line.split()
			starttime=tomin(start.split(":"))
			endtime=tomin(end.split(":"))
			events.append((starttime, DEPART_A))
			events.append((endtime+T, ARRIVE_B))
		
		for i in xrange(NB):
			line=stdin.readline()
			start,end=line.split()
			starttime=tomin(start.split(":"))
			endtime=tomin(end.split(":"))
			events.append((starttime, DEPART_B))
			events.append((endtime+T, ARRIVE_A))
		
		events.sort()
		(A,B)=solve(events)
		print "Case #%d: %d %d" % (case,A,B)
