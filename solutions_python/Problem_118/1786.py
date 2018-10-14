#!/usr/bin/env python

from cmath import sqrt

def nextFair( string ):
	if( len(string) == 1 ):
		temp = int(string) + 1
		string = str(temp)
	
	if( len(string) == 1 ):
		return string
	
	if len(string)%2 == 0:
		first = string[0:len(string)/2];
		fm = first
		second = string[len(string)/2:len(string)]
	else:
		first = string[0:(len(string)-1)/2]
		fm = first + string[(len(string)-1)/2]
		second = string[(len(string)-1)/2+1:len(string)]
		
	if int(first[::-1]) > int(second):			
		if len(string)%2 == 0:
			return fm + fm[::-1]
		return fm + fm[0:len(fm)-1][::-1]
	else:
		fm = int(fm)
		fm+=1
		fm = str(fm)
		
		string = fm+second

		if len(string)%2 == 0:
			fm = string[0:len(string)/2]
		else:
			fm = string[0:(len(string)-1)/2+1]
		
		if len(string)%2 == 0:
			return fm + fm[::-1]
		return fm + fm[0:len(fm)-1][::-1]

T=input()
counter=0

while T:
	T-=1
	counter+=1
	A,B = map(int, raw_input().split())
	
	num = 0
	findSquare = False
	sqrtNum = -1
	
	i=A
	
	while i <= B:
		if str(i) == str(i)[::-1]:
			if findSquare == True:
				if str(sqrtNum) == str(sqrtNum)[::-1]:
					num+=1
			else:
				nn = int(i**(0.5))
				if nn**2 == i:
					findSquare = True
					sqrtNum = nn
					if str(sqrtNum) == str(sqrtNum)[::-1]:
						num+=1
		
		if findSquare == True:
			i += 2*sqrtNum+1
			sqrtNum+=1
		else:
			sqrtNum = int(i**(0.5))
			i = sqrtNum**2
			while i<A :
				i += 2*sqrtNum+1
				sqrtNum+=1
			findSquare = True
			# i = int(nextFair(str(i)))
		
	
	print "Case #{0}: {1}".format( counter, num )
