#! /usr/bin/python
import pickle
import re
f=open('A-large.in','r')

numbers=f.readline().split()
L=int(numbers[0])
D=int(numbers[1])
N=int(numbers[2])

words=[f.readline().rstrip('\n') for i in range(D)]
cases=[f.readline().rstrip('\n').replace('(','[').replace(')',']') for i in range(N)]

a=0
for case in cases:
	a=a+1
	count=0
	for word in words:
		if re.match(case,word):	
			count+=1
	print 'Case #%d: %d'%(a,count)
