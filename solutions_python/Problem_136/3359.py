#!/usr/bin/env python
def printCase (case,msg):
	print "Case #"+str(case)+": "+str(msg)

def calculateResult(cookieBuy, cookieRate, targetCookie):
	first = targetCookie/2;
	buyTimeArray=[]
	rate=2
	second=-1;
	while (second<first):
		if (second != -1): 
			first=second
		buyTimeArray.append(cookieBuy/rate);
		second = sum(buyTimeArray);
		rate+=cookieRate
		second+=targetCookie/rate
	return first

cases = input()
case = 0

while (case<cases):
	case+=1;

	(a,b,c) = map(float,raw_input().split(" "))
	printCase(case,calculateResult(a,b,c))


