#!/usr/bin/python
import operator
import sys
import re
import math
import bisect
from array import array
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input() for i in range(n)]
def read():
	return raw_input()
	
t = int(read())
#data = map(int,readn(t))

def getL(P,miss,cost):
	nmiss = miss[:2**(P-1)]
	ncost = []
	for k in range(1,P):
		ncost += [cost[k][:2**(k-1)]]
	return (P-1,nmiss,ncost)
	
def getR(P,miss,cost):
	nmiss = miss[2**(P-1):]
	ncost = []
	for k in range(1,P):
		ncost += [cost[k][2**(k-1):]]
	return (P-1,nmiss,ncost)

def solve(P, miss, cost):
	#print(getL(P, miss, cost))
	zero = False
	for m in miss:
		if m == 0:
			zero = True
			break
			
	if P == 1:
		if not zero: 
			#print(str(P)+" "+str(miss)+" "+str(cost)+" -> 0")
			return 0
		else: 
			#print(str(P)+" "+str(miss)+" "+str(cost)+" -> "+str(cost[0][0]))
			return cost[0][0]
		
	(pp, lmiss, lcost) = getL(P, miss, cost)
	(pp, rmiss, rcost) = getR(P, miss, cost)
	
	ret = solve(P-1, lmiss, lcost) + solve(P-1, rmiss, rcost) + cost[0][0]
	
	if not zero:
		ret1 = solve(P-1, map(lambda x: x-1, lmiss), lcost) + solve(P-1, map(lambda x: x-1, rmiss), rcost)
		ret = min (ret, ret1)
	
	#print(str(P)+" "+str(miss)+" "+str(cost)+" -> "+str(ret))
	
	return ret
	
for ii in range(t):
	P = int(read())
	miss = map(int, read().split())
	rawcost = readn(P)
	cost = []
	for i in range(P):
		cost = [map(int, rawcost[i].split())] + cost
	#print(P, miss, cost)
	#print(P, len(miss), len(cost))
	print("Case #%s: %s"%(ii+1, solve(P,miss,cost)))

#print(datetime.now()-startTime)