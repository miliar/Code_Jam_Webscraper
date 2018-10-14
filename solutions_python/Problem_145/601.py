#!/usr/bin/env python3
from fractions import gcd
from math import log

rounds = int(input())
for i in range(rounds):
	
	n, d = input().split('/')
	
	n = int(n)
	d = int(d)	
	g = gcd(n,d)
	n = n//g
	d = d//g

	if log(d,2) != round( log(d,2)):
		print("Case #{}: impossible".format(i+1))
		continue;	
	
	while n!=1 :
		n -= 1
		g = gcd(n,d)
		n = n // g
		d = d // g

	print("Case #{}: {}".format(i+1,int(log(d,2))))
 
