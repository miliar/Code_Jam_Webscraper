#!/usr/bin/python
import sys
import math 
from powHash import powHash


def process(N, K):
	#number = int(math.pow(2,N))
	#print (K+1) % number
	
	#number = 2<<(N-1)
	
	try:
		number = powHash[N]
	except:
		number = 2<<(N-1)
	
		
	if((K+1) % number == 0):
		return("ON")
	else:
		return("OFF")
	

if(__name__=="__main__"):
	nTestCases = int(sys.stdin.readline().strip())
		
        for i in range(1,nTestCases+1):
                inputs = sys.stdin.readline().strip().split(" ")
		string = "Case #" + str(i) + ": "
                print string + str(process(int(inputs[0]), int(inputs[1])))
		
		
		

	
