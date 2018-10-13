#!/usr/bin/env python
from math import *

f=open('C-small-attempt0.in','r').readlines()
f1=open('C.out','w')

cnt=0
f=f[1:]
input = len(f)/2
for i in range(input):
	l1=f[i*2].strip().split()
	R=int(l1[0])
	k=int(l1[1])
	group=f[i*2+1].strip().split()

	now = 0
	money=0
	flag=0
	on=[]

	while 1:
		if R == 0:
			flag=1
			break
		if group==[] or now+int(group[0]) > k:
			R=R-1
			money=money+now
			group.extend(on)
			on=[]
			now=0
		else:
			now=now+int(group[0])
			on.append(group[0])
			group.remove(group[0])

	f1.write('Case #'+str(i+1)+': '+str(money)+'\n')
