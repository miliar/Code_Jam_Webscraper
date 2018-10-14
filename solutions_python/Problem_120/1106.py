#!/usr/bin/python

T=int(raw_input())

for i in range(1,T+1):
	split=raw_input().split(" ")
	r=long(split[0])
	t=long(split[1])
	number=0L
	diff=(r+1)**2-r**2
	sum=diff
	while True:
		if(t>=sum):
			number=number+1
		else:
			break;
		diff=diff+4
		sum=sum+diff
	print "Case #"+str(i)+": "+str(number)
