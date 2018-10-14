#!/usr/bin/python

from sys import *

n_cases = int(stdin.readline().rstrip("\n"),10)

for case in range(0,n_cases):
	result="IMPOSSIBLE"
	line = stdin.readline().rstrip("\n").split()
	cakes=line[0]
	ob = int(line[1],10)
	count_r=0

	if '-' not in cakes:
		result=str(0)
	else:
		arr=[]
		for a in cakes:
			arr.append(a)

		for i in range(0,len(arr)):
			if arr[i]=='-':
				if len(arr)<(ob+i):
					result="IMPOSSIBLE"
					break
				else:
					count_r=count_r+1
					for j in range(0,ob):
						if arr[j+i]=='-':
							arr[j+i]='+'
						else:
							arr[j+i]='-'
					result=str(count_r)



	print("Case #"+str(case+1)+": "+result)

