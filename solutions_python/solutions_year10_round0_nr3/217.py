#!/usr/bin/python

C=int(raw_input())

for case in range(C):
	row=raw_input().split()
	R=int(row[0])
	k=int(row[1])
	n=int(row[2])
	row=raw_input().split()
	g=map(int,row)

	result=0
	qs=0	
	for i in range(R):
		fill=0
		first=qs
		if g[qs] > k:
			break

		fill+=g[qs]
		qs=(qs+1)%n

		while ((fill+g[qs])<=k)and (qs!=first):
			fill+=g[qs]
			qs=(qs+1)%n
		result+=fill


	print "Case #"+str(case+1)+": "+str(result)
