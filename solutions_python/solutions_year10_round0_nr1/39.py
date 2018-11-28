#!/usr/bin/python

good = lambda n,k: k%(2**(n))==(2**n-1)

#read=open("input.txt").readline
#out=open("output.txt",'w').write
##read=open("A-small-attempt0.in").readline
##out=open("A-small-attempt0.out","w").write
#read=open("A-small-attempt3.in").readline
#out=open("A-small-attempt3.out","w").write
read=open("A-large.in").readline
out=open("A-large.out","w").write
t=int(read())
for i in xrange(t):
	n,k=map(int,read().split())
	out("Case #%d: %s\n"%(i+1,'ON' if good(n,k) else 'OFF'))
	print i+1

