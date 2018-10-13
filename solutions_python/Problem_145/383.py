#! /usr/bin/env python2.7
from fractions import Fraction

T=int(raw_input())
for test in xrange(1,T+1):
	p_q=Fraction(raw_input())
	q=p_q.denominator
	p=p_q.numerator
	flag=True
	if (p>q or q>2**40):
		flag=False
	else :
		qbin=bin(q)[2:]
		for i in range(1,len(qbin)):
			if (qbin[i]=='1'):
				flag=False
				break
	if flag:
		p_=(2**40)*p/q
		p_bin=bin(p_)[2:]
		n=len(p_bin)-1
		
		
	if flag:
		print "Case #{}: {}".format(test, 40-n)
	else :
		print "Case #{}: impossible".format(test)