#! /usr/bin/env python

import sys

TT=3
T=1
TT=int(sys.stdin.readline())



def mdc(a,b):
	while b != 0:
		c=a
		a=b
		b=c%b
	return a


while T<=TT:
	linha=sys.stdin.readline()
	linha=linha.split()
	N=int(linha[0])

	vals=[]
	for i in range(1,len(linha)):
		vals.append(int(linha[i]))

	vals.sort()

	mdc_tudo=vals[1]-vals[0]
	for i in range(1,len(vals)):
		mdc_tudo=mdc(vals[i]-vals[i-1],mdc_tudo)

	ans=vals[0]%mdc_tudo
	if ans == 0:
		print "Case #" + str(T) + ": " + str( ans)
	else:
		print "Case #" + str(T) + ": " + str(mdc_tudo-vals[0]%mdc_tudo)
	T=T+1
