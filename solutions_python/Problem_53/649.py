#!/usr/bin/python

t=input()
for i in range(1,t+1):
	x=raw_input()
	x=x.split()
	n=int(x[0])
	k=int(x[1])
	temp = 2**n
	k = k%(temp)
	if(k==temp-1):
		print "Case #"+str(i)+": ON"
	else:
		print "Case #"+str(i)+": OFF"





