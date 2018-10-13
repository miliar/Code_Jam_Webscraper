#!/usr/bin/python

T=int(raw_input())
for case in xrange(1,T+1):
	split=raw_input().split(" ")
	N=long(split[0])
	M=long(split[1])
	board=[[0]*M]*N
	row_largest=[0]*N
	col_largest=[0]*M
	result=True
	for row in range(0,N):
		board[row]=map(lambda x:int(x),raw_input().split(" "))
	#Find largest element in each roW
	for i in range(0,N):
		largest=-1
		for j in range(0,M):
			if(board[i][j]>largest):
				largest=board[i][j]
		row_largest[i]=largest
	#Find largest element in each col
	for j in range(0,M):
		largest=-1
		for i in range(0,N):
			if(board[i][j]>largest):
				largest=board[i][j]
		col_largest[j]=largest
	for i in range(0,N):
		for j in range(0,M):
			if(board[i][j]!=min(row_largest[i],col_largest[j])):
				result=False
		if(not result):
			break
	if(result):
		print "Case #"+str(case)+": YES"
	else:
		print "Case #"+str(case)+": NO"
	
