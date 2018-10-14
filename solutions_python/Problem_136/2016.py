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

'''readline Split into float'''
def rlsf(i):
	out=map(float, string.split(i.readline()))
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
oF=2.0 # original cookies rate

for x in range(T):
	[C,F,X]=rlsf(i)
	#print C, oF , F, X
	nF=oF
	timeToBuy=C/nF
	timePassed=timeToBuy
	t=X/nF
	#print "\tnF", nF, "t: ", t,"timeToBuy", timeToBuy, "timePassed", timePassed
	while True:
		# After timePassed, possible time to buy building
		nF+=F
		nT=timePassed+X/nF
#		print "\tnF", nF, "t: ", t,"nT:", nT, "timeToBuy", timeToBuy, "timePassed", timePassed
		if nT > t:
			#print "\tnF", nF, "t: ", t,"nT:", nT, "timeToBuy", timeToBuy, "timePassed", timePassed
			break
		timeToBuy=C/nF
		timePassed+=timeToBuy
		t=nT
		
		

	z=8#map(translate,temp)
	wout(o, x+1, "{0:.7f}".format(t))

