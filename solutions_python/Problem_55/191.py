#!/usr/bin/python

import sys
def rollerTest(k,R,G):
	if(k>sum(G)):
		return R*sum(G)
	Q=G*(R+1)
	c=0
	for i in range(0,R):
		s=0
		while (s+Q[0]<=k):
			s+=Q.pop(0)
		c+=s
	return c
		
			
fin=open(sys.argv[1]+'.in')
fout=open(sys.argv[1]+'.out','w')

n=int(fin.readline().strip())
for i in range(0,n):
	R,k,N=tuple([int(j) for j in fin.readline().strip().split(' ')])
	G=[int(j) for j in fin.readline().strip().split(' ')]
	fout.write("Case #%d: %s\n"%(i+1,rollerTest(k,R,G)))
fout.close()
