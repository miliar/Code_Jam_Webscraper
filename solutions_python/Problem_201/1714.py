# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:59:29 2017

@author: adobe
"""
magic = lambda nums: int(''.join(str(i) for i in nums))
from math import *
N=input()
ans=[]
for i in range(N):
	nk=raw_input()
	# n=input()
	# k=input()
	(n,k)=nk.split(' ')
	n=int(n)
	k=int(k)
	tmp=int(k)
	h=int(log(tmp,2))
	kp=pow(2,h)-1
	det=(n-kp)%pow(2,h)
	if det==0:
		dt=(n-kp)/pow(2,h)
	else:
		t=det
		if k-kp>t:
			dt=(n-kp)/pow(2,h)
		else:
			dt=(n-kp)/pow(2,h)+1
	dmin=int(dt-1)/2
	dmax=int(dt)-1-dmin


	ans.append([dmax,dmin])
# print ans

for j,con in enumerate(ans):
	print "Case #"+str(j+1)+": "+str(con[0])+" "+str(con[1])