#!/usr/bin/env python

import sys

global a,b
f= open(sys.argv[1])
outp = open(sys.argv[1]+'.out.txt','w')
T= int(f.next())
cnt=0
bds=[]

def rts(s):
	l=len(s)
	sl=[]
	for x in range(1,l):
		r=s[x:]+s[:x]
		if r not in sl:
			sl.append(r)
	return sl

def fc(m):
	possible=0
	m_s=str(m)
	mds=[ int(x) for x in m_s]
	sl=rts(mds)
	for nds in sl:
		if mds==nds:
			continue
		flag=True
		for y in range(len(mds)):
			if nds[y]>mds[y]:
				break
			if nds[y]==mds[y]:
				continue
			flag=False
			
		if flag:
			for y in range(len(mds)):
				if nds[y]<bds[y]:
					break
				if nds[y]==bds[y]:
					continue
				flag=False
		if flag:
			possible+=1
	return possible
		
	
while(cnt<T):
	cnt+=1
	(a,b)=[ int(x) for x in f.next().split()]
	possible=0
	m=a
	bds=[ int(x) for x in str(b)]
	while(m<=b):
		possible += fc(m)
		m+=1
	print 'Case #'+str(cnt)+': '+ str(possible)
	outp.write('Case #'+str(cnt)+': '+ str(possible)+'\n')
outp.close()
