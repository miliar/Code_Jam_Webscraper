#!/usr/bin/python

import sys

def snapTest(N,K):
	return (K%(2**N))==(2**N-1)

fin=open(sys.argv[1]+'.in')
fout=open(sys.argv[1]+'.out','w')

n=int(fin.readline().strip())
for i in range(0,n):
	N,K=tuple([int(j) for j in fin.readline().strip().split(' ')])
	fout.write("Case #%d: %s\n"%(i+1,("ON" if snapTest(N,K)else "OFF")))
fout.close()
	
