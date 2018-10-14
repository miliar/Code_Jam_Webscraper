# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:59:29 2017

@author: adobe
"""
import numpy as np
import copy
magic = lambda nums: int(''.join(str(i) for i in nums))
from math import *
N=input()
ans=[]
	
f = open('tryD.out', 'w')


def takeafter(cake,R,C,cp):
	if cp<C:
		if cake[0,cp]==0:
			cake[:,cp]=takeafter(cake,R,C,cp+1)
		return cake[:,cp]
	else:
		return np.zeros([R])
def takebefore(cake,R,C,cm):
	if cm>=0:
		if cake[0,cm]==0:
			cake[:,cm]=takebefore(cake,R,C,cm-1)
		return cake[:,cm]
	else:
		return np.zeros([R])
			


for i in range(N):
	sen=raw_input()
	(R,C)=sen.split()
	R=int(R)
	C=int(C)
	cake=np.zeros([R,C])

	for r in range(R):
		sen2=raw_input()
		ls=list(sen2)
		ls2=[ord(a) for a in ls]
		#print "ls2", ls2
		cake[r]=ls2
	cake-=63
	#print "cake ", cake

	for r in range(R):
		for c in range(C):
			if cake[r,c]!=0:
				rplus=r+1;
				rminus=r-1;
				if rplus<R:
					while cake[rplus,c]==0 and rplus<R:
						cake[rplus,c]=cake[r,c]
						rplus+=1
						if rplus>=R:
							break
				if rminus>=0:
					while cake[rminus,c]==0 and rminus>=0:
						cake[rminus,c]=cake[r,c]
						rminus-=1
						if rminus<0:
							break
	for c in range(C):
		if cake[0,c]==0:
			cplus=c+1
			cminus=c-1
			if cplus<C:
				cake[:,c]=takeafter(cake,R,C,cplus)
			if cake[0,c]!=0:
				continue
			if cminus>=0:
				cake[:,c]=takebefore(cake,R,C,cminus)
	
	#print "cake afterwards", cake
	cake+=63
	# ans.append(cake)
	print >>f,"Case #"+str(i+1)+": "
	for r in range(R):
		line=cake[r].tolist()
		print >>f,"".join([chr(int(a)) for a in line])
		# for c in range(C):
		# 	print >>f,chr(int(cake[r,c])),

	
	



# for j,con in enumerate(ans):
## 	# print "Case #"+str(j+1)+": "+str(scores[j])+" "+str(len(con))
# 	# for jj in con:
## 		# print jj
## 	print >>f,"Case #"+str(j+1)+": "
# 	(R,C)=sen.split()
# 	R=int(R)
# 	C=int(C)
# 	for r in range(R):
# 		for c in range(C):
## 			print >>f,chr(int(ans[j][r,c])),
## 		print >>f




f.close()