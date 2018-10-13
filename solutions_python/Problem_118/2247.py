from math import *

def isPalindrome(digits):
	length = len(digits)
	for i in range(0,int(length/2)+1):
		if digits[i]!=digits[length-1-i]:
			return False
	#print digits
	return True

fi = open('input.txt','r')
fo = open('output.txt','w')
t = int(fi.readline())
for i in range(0,t):
	rng = map(int,fi.readline().split())
	originBegin = int(ceil(sqrt(rng[0])))
	originEnd = int(floor(sqrt(rng[1])))
	originList = range(originBegin,originEnd+1)
	#squareList = map((lambda x: x*x), originList)
	result = 0
	for k in originList:
		if isPalindrome(map(int,list(str(k)))) and isPalindrome(map(int,list(str(k*k)))):
			result+=1
	print "Case #{0}: {1}".format(i+1,result)

fi.close
fo.close