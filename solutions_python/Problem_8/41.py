#!/usr/bin/python2.5
import sys
import bisect
import math

inputName = "test.in" if (len(sys.argv) < 2) else sys.argv[1]
file = open(inputName, "r")

def readline(): return file.readline().strip(" \n")

for case in range(int(readline())) :
	A, B, P = map(int, readline().split())
	
	mas = [False] * (B - A + 1)
	marked =set([])
	
	def IsPrime(x):
		for i in range(2, int(math.sqrt(x)) + 1):
			if (x % i == 0):
				return False
		return True
	
	def AddAll(n):
		if n >= A and n <= B and mas[n - A]:
			return;
		
		for i in range(P, n + 1):
			if ((n % i == 0) and IsPrime(i)):
				Mark(i)
				
	def Mark(k):
		if (k in marked):
			return
		marked.add(k)
		start = (A / k) * k
		if (start < A): start += k;
			
		while (start <= B):
			if (not mas[start - A]):
				mas[start - A] = True;
				AddAll(start / k)
			start += k
				
				
	res = 0
	
	for i in range(A, B + 1):
		if (not mas[i - A]):
			AddAll(i)
			res+= 1;
	
					
	print "Case #%s: %s" % (case + 1,  res)
	

	