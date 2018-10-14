#!/usr/bin/python
#
# Google CodeJam 2010
#  Round 1C
#  Problem C
#
# Author: David Volgyes
#

import sys,os,numpy
from sympy.geometry import *

def hexaToBin(hexaNum):
	if hexaNum=="0": return "0000"
	if hexaNum=="1": return "0001"
	if hexaNum=="2": return "0010"
	if hexaNum=="3": return "0011"
	if hexaNum=="4": return "0100"
	if hexaNum=="5": return "0101"
	if hexaNum=="6": return "0110"
	if hexaNum=="7": return "0111"
	if hexaNum=="8": return "1000"
	if hexaNum=="9": return "1001"
	if hexaNum=="A": return "1010"
	if hexaNum=="B": return "1011"
	if hexaNum=="C": return "1100"
	if hexaNum=="D": return "1101"
	if hexaNum=="E": return "1110"
	if hexaNum=="F": return "1111"
	return "0000"

def markUsed(arr,x,y,S,M,N):
	l=len(arr)
	for i in range(x,x+S):
		for j in range(y,y+S):
			arr[i,j]=2
	return arr

def checkArray(arr,x,y,S,M,N):
	if (x+S>M) or (y+S>N): return False
	result=True
	if arr[x,y]==2: return False
	for i in range(x,x+S-1):
		for j in range(y,y+S-1):
			if arr[i,j]+arr[i+1,j]!=1: return False
			if arr[i,j]+arr[i,j+1]!=1: return False
			if arr[i,j]!=arr[i+1,j+1]: return False
	return True

def stringToBin(hexa,M):
	result=""
	for i in range(0,len(hexa)):
		result=result+hexaToBin(hexa[i])
	return result

T=int(sys.stdin.readline().strip())
for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	M=int(inputwords[0])
	N=int(inputwords[1])
	array=numpy.zeros((M,N))
	for i in range(0,M):
		line=sys.stdin.readline().strip()
		hexa=stringToBin(line,M)
		for c in range(0,len(hexa)):
			if hexa[c]=="0":
				array[i,c]=0
			else:
				array[i,c]=1
	res=dict()
	for m in range(0,M):
		m2=M-m
		res[m2]=0
		for i in range(0,M-m2+1):
			for j in range(0,N-m2+1):
				if checkArray(array,i,j,m2,M,N):
					res[m2]=res[m2]+1
#					print(array)
					array=markUsed(array,i,j,m2,M,N)
#					print(array)
#					sys.exit(-1)
		if res[m2]==0: del res[m2]
	result=0
	print("Case #%i: %i" % (case,len(res)))
	resKeys=res.keys()
	resKeys.reverse()
	for k in resKeys:
		print("%i %i" % (k,res[k]))
