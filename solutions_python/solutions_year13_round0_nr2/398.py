import sys
import os

def process(a):
	rowmax=[]
	for i in a:
		rmax=-1
		for j in i:
			rmax=max(j,rmax)
		rowmax.append(rmax)
	ta=zip(*a)
	colmax=[]
	for i in ta:
		cmax=-1
		for j in i:
			cmax=max(j,cmax)
		colmax.append(cmax)
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j]!=colmax[j] and a[i][j]!=rowmax[i]:
				return 'NO'
	return 'YES'
		

tcases=int(sys.stdin.readline())

for case in range(tcases):
	n,m=map(int,sys.stdin.readline().split())
	a=[]
	for line in range(n):
		a.append(map(int,sys.stdin.readline().split()))
	print 'Case #'+str(case+1)+': '+process(a)


		
	
