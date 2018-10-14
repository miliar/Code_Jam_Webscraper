
from concurrent import futures
import time
import os,sys
import grpc
import json
def getdigital(num,length,digital):
	rest=num
	for i in range(length,0,-1):
		if i==0: 
			return
		dig=rest/(10**(i-1))
		digital[length-i]=dig
		rest=rest-dig*10**(i-1)
		
def checktide(digital):
	tide=1
	pre=0
	for i in range(len(digital)):
		if digital[i]<pre:
			return 0
		pre=digital[i]
	return tide


def gettide(number):
	num=int(number)
	
	for i in range(num,0,-1):
		num_len=len(str(i))
		digital=[1]*num_len
		getdigital(i,num_len,digital)
		check=checktide(digital)
		if check == 1:
			return i
	return -1

if __name__ == '__main__':
	c = raw_input("")
	count = int(c)
	number = [1]*count
	tidenumber=[1]*count
	for i in range(0, count):
		number[i]=raw_input("")
		tidenumber[i]=gettide(number[i])
	for i in range(0, count):
		print("Case #%d: %s"%(i+1,tidenumber[i]))
