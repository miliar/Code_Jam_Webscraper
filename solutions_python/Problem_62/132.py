#!/usr/bin/env python
import math
import sys
import os
from os import system

def mergeAndCount(A,B):
	i = 0
	j = 0
	count = 0
	C = []
	while len(A) != i and len(B) != j:
		C.append(min(A[i],B[j]))
		if B[j] < A[i]:
			count = count + len(A)-i
			j  = j + 1
		else :
			i = i + 1
	print C
	if len(A) == i:
		if len(B) == j+1:
			C.append(B[j])
		else :
			if j == 0:
				rest = B
			else :
				rest = B[j-1:]
			for l in rest:
				C.append(l)
	else :
		if len(A) == i+1:
			C.append(A[i])
		else :
			if i == 0:
				rest = A
			else :
				rest = A[i-1:]
			for l in rest:
				C.append(l)
	return count, C

def sortAndCount(L):
	#print L
	n = len(L) 
	#print n
	if n == 1:
		return 0,L
	else :
		m = n/2
		A = L[:m]
		B = L[m:]
		rA,A = sortAndCount(A)
		#print rA,A
		rB,B = sortAndCount(B)
		#print rB,B
		r,L = mergeAndCount(A,B)
		rr = rA + rB + r
	return rr,L


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	N = int(l[0])
	point = []
	for j in range(N):
		l = fp.readline().split()
		point.append((int(l[0]),int(l[1])))
	points = sorted(point, key = lambda p:p[0])
	print points
	B = []
	for j in range(N):
		B.append(points[j][1])
	#print B
	num,L = sortAndCount(B)
	#print L
	fout.write('Case #%d: %d\n'%(i+1,num))

