#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: python run.py < A-small-practice.in > result.txt

def solve(c,f,x):
	
	nf = 0
	tinvest = 0		
	
	while (True):				

		tx = x / (2 + nf * f) 				
		t = tinvest + tx;

		#print("Nf=%i, Time Invested=%.5f, Time To X With Farms=%.5f, Total=%.5f" % (nf, tinvest, tx, t))	
		tinvest += c / (2 + nf * f)

		nf += 1
		
		tx = x / (2 + nf * f) 
		tnext = tinvest + tx

		if (t < tnext):			
			break
		else:
			t = tnext	

	return t

testcases = input()
     
for caseNr in xrange(1, testcases+1):
    c, f, x = raw_input().split(' ')   

    print("Case #%i: %.7f" % (caseNr, solve(float(c),float(f),float(x))))
