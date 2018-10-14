#!/usr/bin/python
#
# Google CodeJam 2010
#  Round 1A
#  Problem A
#
# Author: David Volgyes
#

import sys,os,numpy
from sympy.geometry import *

def rotate(field,direction,N):
	result=list()
	if direction%4==0:
		for i in range(0,N+1):
			row=list()
			for j in range(0,N+1):
				row.append(field[i][j])
			result.append(row)
	if direction%4==1:
		for i in range(0,N+1):
			row=list()
			for j in range(0,N+1):
				row.append(field[j][N-i])
			result.append(row)
	if direction%4==2:
		for i in range(0,N+1):
			row=list()
			for j in range(0,N+1):
				row.append(field[N-i][N-j])
			result.append(row)
	if direction%4==3:
		for i in range(0,N+1):
			row=list()
			for j in range(0,N+1):
				row.append(field[N-j][i])
			result.append(row)
	return result

def gravity(rfield):
	result=numpy.matrix(rfield)
	localN=len(rfield)
	for i in range(0,localN):
		for j in range(0,localN):
			result[i,j]=0

	for i in range(0,localN):
		k=localN-1
		for j in range(0,localN):
			j2=localN-1-j
			if rfield[j2][i]==0: continue
			result[k,i]=rfield[j2][i]
			k=k-1
	return result

def win2(grfield,i,j,lN,player,K):
	if j+K<=lN:
		result1=True
		for k in range(0,K):
			if grfield[i,j+k]!=player:
				result1=False
	else:
		result1=False

	if (j+K<=lN) and (i+K<=lN):
		result2=True
		for k in range(0,K):
			if grfield[i+k,j+k]!=player:
				result2=False
	else:
		result2=False

	if (i+K<=lN):
		result3=True
		for k in range(0,K):
			if grfield[i+k,j]!=player:
				result3=False
	else:
		result3=False

	if (j+K<=lN) and (i+K<=lN):
		result4=True
		for k in range(0,K):
			if grfield[i+K-k-1,j+k]!=player:
				result4=False
	else:
		result4=False
	return result1 or result2 or result3 or result4


def win(rfield,player,K):
	grfield=gravity(rfield)
	localN=len(rfield)
	result=False
	for i in range(0,localN):
		for j in range(0,localN):
			result=win2(grfield,i,j,localN,player,K)
			if result: break
		if result: break
	return result

def Solve(N,K,field):
	blue=False
	red=False
	for i in range(3,4):
		rfield=rotate(field,i,N-1)
		if win(rfield,1,K):red=True
		if win(rfield,2,K): blue=True
		if red  and blue: break
	if red and blue: result="Both"
	if red and blue==False: result="Red"
	if red==False and blue: result="Blue"
	if red==False and blue==False: result="Neither"
	return result

T=int(sys.stdin.readline())

for case in range(1,T+1):
	inputwords=sys.stdin.readline().strip().split()
	N=int(inputwords[0])
	K=int(inputwords[1])
	field=list()
	for i in range(0,N):
		row=list()
		inputwords=sys.stdin.readline().strip()
		for j in range(0,len(inputwords)):
			if inputwords[j]=='.': row.append(0)
			if inputwords[j]=='R': row.append(1)
			if inputwords[j]=='B': row.append(2)
		field.append(row)
	result=Solve(N,K,field)
	print("Case #%i: %s" % (case,result))
