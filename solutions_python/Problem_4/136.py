#!/usr/bin/env python

inf=file('A-large.in','r')
outf=file('A-large.out','w')
casenum=int(inf.readline())
for T in range(0,casenum):
	n=int(inf.readline())
	A=0
	x=[]
	y=[]
#	tmp=inf.readline()
#	for i in range(0,n):
#		x.append(int(tmp.split(' ')[i]))
#	tmp=inf.readline()
#	for i in range(0,n):
#		y.append(int(tmp.split(' ')[i]))
	x=[ int(t) for t in inf.readline().split(' ') ]
	y=[ int(t) for t in inf.readline().split(' ') ]
	x.sort()
	y.sort()
	for i in range(0,n):
		A+=x[i]*y[n-i-1]
		if(i!=n-i-1):
			A+=y[i]*x[n-i-1]
		if(i+1>=n-i-1):
			break
	
	outf.write('Case #%d: %d\n'%(T+1,A))
inf.close()
outf.close()
