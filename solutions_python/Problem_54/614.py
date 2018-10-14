#!/usr/bin/env python
import math
import sys
import os
from os import system

fp = open('B-small-attempt1.in','r')
fout = open('b.out','w')
str = fp.readline()
C = int(str)
for i in range(C):
	l = fp.readline().split()
	N = int(l[0])
	t = []
	nn = []
	tmin = 10**50
	nnmax = 0
	jmin = 0
	maxg = 1
	for j in range(N):
		nn.append(int(l[j+1]))
		if nn[j] > nnmax:
			nnmax = nn[j]
	print nn
	print nnmax
	for j in range(N):
		for k in range(N-j-1):
			if (nn[j] - nn[j+k+1]) != 0:
				t.append(abs(nn[j] - nn[j+k+1]))
	print t
	NN =  len(t)#(N*(N-1))/2
	for j in range(NN):
		if t[j] < tmin:
			tmin = t[j]
			jmin = j
	if NN == 1:
		maxg = t[0]
	else :
		t.sort()
		ok = 0
		for j in range(NN):
			ok = 0
			for k in range (NN-j-1):
				if t[j] > t[j+k+1]:
					mb = t[j]
					ms = t[j+k+1]
				else :
					mb = t[j+k+1]
					ms = t[j]
				print mb 
				print ms
				r = ms
				while 1:
					tmp = 0
					while tmp + ms <= mb:
						tmp = tmp + ms
					g = r
					r = mb - tmp
					if r == 0:
						break
					else :
						mb = ms
						ms = r
				print "%d %d" %(t[j],t[j+k+1])
				print g
				l = j+k+1 + 1
				ok = 1
				while l < NN:
					if t[l]%g != 0:
						ok = 0
						break
					l = l + 1
				if ok == 1:
					maxg = g
					break
			if ok == 1:
				break

		maxg = g

	
	temp = 0
	while temp < nnmax:
		temp = temp+maxg
	print temp
		
	fout.write('Case #%d: %d\n'%(i+1,temp-nnmax))
