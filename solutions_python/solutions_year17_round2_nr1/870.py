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




for i in range(N):
	sen=raw_input()
	(R,nnp)=sen.split()
	tslow=-1
	nslow=-1
	R=int(R)
	nnp=int(nnp)
	info=np.zeros([nnp,2])
	for ii in range(nnp):
		sen=raw_input()
		(x,v)=sen.split()

		x=int(x)
		v=int(v)
		info[ii]=np.array([x,v])
	for r in range(nnp):
		(x,v)=info[r]
		tthis=(R-x)*1.0/v
		if tslow==-1:
			tslow=tthis
			nslow=r
			continue
		else:
			if tslow<tthis:
				tslow=tthis
				nslow=r
	(x,v)=info[nslow]
	vmax=R/(R-x)*v
	ans.append(vmax)

# print ans




	



for j,con in enumerate(ans):
	print >>f, "Case #"+str(j+1)+": "+str(ans[j])
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