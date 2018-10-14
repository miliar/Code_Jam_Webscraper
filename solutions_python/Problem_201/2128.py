#!/usr/bin/python

from sys import *

n_cases = int(stdin.readline().rstrip("\n"),10)

for case in range(0,n_cases):
	result1=0
	result2=0
	line = stdin.readline().rstrip("\n").split()
	stalls=int(line[0],10)
	mans = int(line[1],10)
	arr=[]
	arr.append(stalls)

	for i in range(0,mans):
		max_n=max(arr)
		arr.remove(max_n)

		result1=max_n/2
		if (max_n-1)==0:
			result2=0
		else:
			result2=(max_n-1)/2

		arr.append(result1)
		arr.append(result2)

		#print(arr)



	print("Case #"+str(case+1)+": "+str(result1)+" "+str(result2))

