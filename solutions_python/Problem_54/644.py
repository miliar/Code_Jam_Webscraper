#!/usr/bin/env python
from math import *
from fractions import *


f=open('B-small-attempt0.in','r').readlines()
f1=open('B.out','w')
l=f[0]

cnt=0
for line in f[1:]:
	cnt=cnt+1
	num = line.strip().split()[1:]
	diff=[]
	for i in range(len(num)):
		num1=int(num[i])
		for j in num[i+1:]:
			num2 = int(j)
			diff.append(abs(num1-num2))
	gg=diff[0]
	for i in diff:
		gg=gcd(gg,i)

	ggg=gg
	while 1:
		if ggg>=int(num[0]):
			break
		ggg=ggg+gg
	ans = ggg-int(num[0])
	for i in num:
		i=int(i)+ans
		if i%gg!=0:
			print 'wrong'
		
	f1.write('Case #'+str(cnt)+': '+str(ans)+'\n')
