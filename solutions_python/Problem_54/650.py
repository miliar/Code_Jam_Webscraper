#!/usr/bin/python
from math import pow 
from string import atoi
from math import ceil 
from decimal import *

data = open('input')
data.readline()
out = open('out', 'w')
n = 1

D = Decimal
getcontext().prec = 70
def recgcd(a,b=0,*values):
	if b==0:
		return a
	while b != 0:
		rb = a%b
		a = b
		b=rb
	if values:
		low = recgcd(a,*values) 
		if a < low:
			return a
		return low
	return a
	
for case in data.readlines():
	strtimes = case.rsplit()
	times = []
	for t in strtimes:
		t = atoi(t)
		times.append(t)
	times = times[1:]
	times.sort(reverse=True)
	
	a=0
	deltas=[]
	for t in times:
		if a==0:
			a=t
		else:
			deltas.append(a-t)
			a=t
	gcd = recgcd(*deltas)	
	
		
	hi = times[0]

	nextval =D(hi)/D(gcd)
	nextval = nextval.quantize(D('1.'), rounding=ROUND_UP)	

	print nextval
	
	T=nextval*D(gcd)-D(hi)
	print hi,gcd,T

	out.write("Case #%d: %d\n"%(n,T))
	n+=1
