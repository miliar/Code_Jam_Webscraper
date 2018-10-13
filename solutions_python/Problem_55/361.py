#!/usr/bin/python

import sys


for tcase in range(input()):
	ln=raw_input().split(' ')
	
	R=int(ln[0]);
	k=int(ln[1]);
	N=int(ln[2]);
	
	g=[int(t) for t in raw_input().split(' ')]

	done=[0]*N;
	
	next=lambda x:(x+1)%N;
	
	starts=[]
	earn=[]
		
	#print 'g=',g
	#print 'k=',k
	
	start=0;
	cstart=-1;
	while 1:
		s=0
		i=start
		while 1:
			if(s+g[i]<=k):
				s+=g[i]
				i=next(i)
			else:
				break
			if(i==start):
				break;

		starts.append(start)
		earn.append(s)
		done[start]=1
		
		if done[i]:
			cstart=i
			break
		start=i
	
	for i in range(len(starts)):
		if starts[i]==cstart:
			cstart=i;
			break

	e=[earn[0:cstart],earn[cstart:len(earn)]]

	res=0;
	if(R<=len(e[0])):
		res=sum(e[0][0:R]);	
	else:
		res=sum(e[0]);
		R-=len(e[0]);
		earn=e[1];
		res+=(R/len(earn))*sum(earn)+sum(earn[0:(R%len(earn))])
		
	sys.stdout.write('Case #%d: %d\n'%(tcase+1,res))
			
	
	
	
