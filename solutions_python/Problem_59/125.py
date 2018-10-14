#!/usr/bin/python

T=int(raw_input())

for case in range(T):
	row=raw_input().split()
	n=int(row[0])
	m=int(row[1])
	root={}

	for i in range(n):
		row=raw_input()[1:].split('/')
		dp=root
		for sd in row :
			if not(sd in dp):
				dp[sd]={}
			dp=dp[sd]

	out=0

	for i in range(m):
		row=raw_input()[1:].split('/')
		dp=root
		for sd in row:
			if not (sd in dp):
				out+=1
				dp[sd]={}
			dp=dp[sd]
				 

	print "Case #"+str(case+1)+": "+str(out)
			

