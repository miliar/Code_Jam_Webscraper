#!/usr/bin/python
import sys
arr=[]
j=0
first=True
for lines in sys.stdin:
	if first:
		T=int(lines)
		first=False
	else:
		arr.append(lines.split())
for i in range(T):
	N=int(arr[i*3][0])
	list1=arr[i*3+1]
	list2=arr[i*3+2]
	list11,list22=[],[]
	for elem in list1:
		list11.append(float(elem))
	for elem in list2:
		list22.append(float(elem))
	list11.sort()
	list22.sort()
	k=0
	M=N
	cnt=0
	for elem in list11:
		if elem > list22[k]:
			cnt=cnt+1
			k=k+1
	deciet=cnt
	k=0
	cnt=0
	for elem in list11:
		while k < N and elem > list22[k]:
			cnt=cnt+1
			k=k+1
		k=k+1
		if k >=N:
			break
	print "Case #%d: %d %d" %(i+1,deciet,cnt)
