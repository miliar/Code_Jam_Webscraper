#!/usr/bin/python
import fileinput
import sys
import numpy
import copy
import math
import string

def prt(txt):
	sys.stdout.write(txt);



def main():
	count = int(raw_input())

	for c in range(0,count):
		prt("Case #" + str(c + 1)+": ")

		[Ps, Qs] = string.split(raw_input(),'/')
		(P, Q) = (int(Ps), int(Qs))

		q = Q
		p = P
		valid = True
		generations = 0
		while(q > 1):
			if q % 2 != 0:
				#prt("Not divisible by 2: "+str(q)+" with p="+str(p)+"\n")
				foundFactor = False	
				for i in range(3,q+1):
					if q % i == 0 and p % i == 0:
						#prt("Common factor: "+str(i)+"\n")
						q /= i;
						p /= i;
						foundFactor = True
						break;

				if not foundFactor:
					valid = False
					break;
			else:
				q /= 2;
				generations += 1;

		while(p > 1):
			p =  int(p / 2);
			generations -= 1;

		if valid:
			prt(str(generations)+"\n")
		else:
			prt("impossible\n")



main()