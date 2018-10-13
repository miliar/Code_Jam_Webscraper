# -*- coding: utf-8 -*-
from math import *
import re

fin = open("C-small-attempt8.in")
fout = open("C-small-attempt8.out","w")

#fin = open("C-large.in")
#fout = open("C-large.out","w")

cases= int(fin.readline().split()[0])
case = 0

def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result
 


def answer(x):
	global case, cases
	case += 1
	print >>fout, "Case #"+str(case)+": "+str(x)
	print "Case #"+str(case)+": "+str(x)
	
for test in xrange(cases):
	n,l,h = map(int, fin.readline().split())
	c = map(int, fin.readline().split())
	d=c
	pr=1;
	vale=False
	if (l==1):
		answer(1)
		continue
	f=1
	prim=[1]
	d.sort()
	for ii in d:
		if (f):
			pr=lcm(pr,ii)
			aux=pr
			i=l/aux
			while aux*i<h:
				pr=aux*i
				i+=1
				vale=True
				for k in xrange(n):
					vale=vale and (pr%d[k]==0 or d[k]%pr==0 )
				if (vale and pr>=l and pr<=h):
					f=0
					answer(pr)
					break
			pr=aux
	if (f):	answer("NO")	
	
	
	
	
	
	
	
	
	
	
	
	
	


