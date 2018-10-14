#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
	out=map(int, string.split(i.readline()))
	return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, arg):
	out="Case #"+ str(i)+":"
	out+=" "+str(arg)
	#out+=" "+''.join(arg)
	#for arg in args:
	#    out+=" "+str(arg)
	out+="\n"
	o.write(out)

T=rls(i)

for x in range(T):
	firstAns=rls(i)
	#print firstAns
	# skip uninterested line
	for xx in range(firstAns-1):
		i.readline()
	c1=rls(i)
	#print c1
	# skip uninterested lines
	for xx in range(4-firstAns):
		i.readline()

	secAns=rls(i)
	#print secAns
	# skip uninterested line
	for xx in range(secAns-1):
		i.readline()
	c2=rls(i)
	#print c2
	# skip uninterested lines
	for xx in range(4-secAns):
		i.readline()

	c3=list(set(c1)&set(c2))
	#print c3
	lc3=len(c3)
	#print lc3
	z=""
	if lc3 == 0:
		z="Volunteer cheated!"
	elif lc3 == 1:
		z=c3[0]
	else:
		z="Bad magician!"
	wout(o, x+1, z)

