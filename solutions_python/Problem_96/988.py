#!/usr/bin/env python

import sys
f= open(sys.argv[1])
outp = open(sys.argv[1]+'.out.txt','w')
T= int(f.next())
cnt=0
while(cnt<T):
	cnt+=1
	dat=f.next().split()
	nums=[int(x) for x in dat]
	(n,s,p)= nums[:3] 
	tis=nums[3:]
	nm=3*p-2
	sm=3*p-4
	if nm<1:
		nm=1
	if sm<1:
		sm=1
	possible=0
	for x in tis:
		if x >= nm:
			possible+=1
		else: 
			if x >= sm and s:
				possible+=1
				s-=1
	if p==0:
		possible = n
	print 'Case #'+ str(cnt) +': '+str(possible)
	outp.write( 'Case #'+ str(cnt) +': '+str(possible)+'\n')
outp.close()
		
