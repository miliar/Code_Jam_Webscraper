#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
	out=map(int, string.split(i))
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

T=rls(i.readline())

'''The function to solve the problem'''
def solve ( args ):
	smax = int(args[0])
	ss = args[1]
	mp2i_i=0	# Temp minPeople2Invite at index i
	numSO_i=0	# number of standing ovation (SO) at index i
	for s in range(smax+1):
		# numSO_i is the number of SO at index s-1
		mp2i_i=max(s-numSO_i, mp2i_i)
		# Update number of SO
		numSO_i+=int(ss[s])
	return mp2i_i

for x in range(T):
	temp=i.readline()
	z=solve(string.split(temp))
	wout(o, x+1, z)

