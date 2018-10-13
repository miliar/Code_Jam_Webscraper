#!/usr/bin/python
import math as m
import numpy as n
import random as r

def solve(a,b):
	answer = 0


	low = int(m.ceil(n.sqrt(a)))
	high = int(m.floor(n.sqrt(b)))


	#Testing testing!!!

	low = 367453
	high = 4938654906859078

	
	print '(' + str(low) + ',' + str(high) + ')';

	HZ = len(str(high))
	LZ = len(str(low))

	full_chunks = HZ - LZ - 1;

	print "Full chunks: " + str(full_chunks)

	if full_chunks > 0:
		for i in range(1,full_chunks+1):
			d = int(m.floor(LZ+i)/2)
			answer = answer + 9*(10**d)

	print "Answer: " + str(answer)
	print '\n'



	answer_low = 1
	choices2 = []
	for i in range(0,LZ):
		choices2.append(int(str(low)[i]))

	r = int(m.ceil(float(LZ)/2))

	for i in range(0,r):
		print (10-choices2[i]-1) * (10**(r-i-1))
		

	print answer_low



	answer = 0
	return 0




def solvesimple(a,b):
	answer = 0

	low = int(m.ceil(n.sqrt(a)))
	high = int(m.floor(n.sqrt(b)))

	print '(' + str(low) + ',' + str(high) + ')';


	answer = 0

	for i in range(low,high+1):
		si = str(i)
		l = len(si)

		if(l == 1):
			if(ispalindrome(str(i**2))):
				answer = answer + 1
			continue
		
		if(l%2 == 0):
			if(i%11 == 0):
				if(ispalindrome(si)):
					if(ispalindrome(str(i**2))):
						answer = answer + 1
		else:
			sishort = si[0:l/2] + si[l/2+1:l]
			sishort = int(sishort)
			if(sishort % 11 == 0):
				if(ispalindrome(si)):
					if(ispalindrome(str(i**2))):
						answer = answer + 1
				
	return answer

def ispalindrome(x):
	n = len(x)
	for i in range(0,n/2):
		if(x[i] != x[n-(i+1)]):
			return 0
	return 1


def solvedeceptive(a,b):
	answer = 0
	allanswers = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004]
	for i in allanswers:
		if(a <= i and i <= b):
			answer = answer + 1
	return answer

f = open('input.txt');
o = open('output.txt','w')

i = 0
for lines in f:


	if(i == 0):
		i = i + 1 
		testcases = lines
		continue
	i = i + 1
	upper = float(lines.partition(" ")[2])
	lower = float(lines.partition(" ")[0])
	o.write("Case #" + str(i-1) + ": " + str(solvedeceptive(lower,upper))+ "\n") 

	# for i in range(1,10000000):
	# 	if(ispalindrome(str(i))):
	# 		if(ispalindrome(str(i**2))):
	# 			print i**2


