#!/usr/bin/python

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	N=int(row[0])
	K=int(row[1])
	B=int(row[2])
	T=int(row[3])

	Xi=map(int,raw_input().split())
	Vi=map(int,raw_input().split())

	Ti=[0]*N
	for i in range(N):
		Ti[i]=(B-Xi[i])/float(Vi[i])

	intime=0
	swps=0
	out=0

	i=N-1
	while((not(i<0))and(K>intime)):
		if Ti[i]<=T:
			intime+=1
			out+=swps
		else:
			swps+=1
		i-=1


	if K>intime:
		print "Case #"+str(case+1)+": IMPOSSIBLE"
	else:
		print "Case #"+str(case+1)+": "+str(out)
			

