#!/usr/bin/python
from math import sqrt
test=input();
for j in range(1,test+1):
	a=raw_input();
	l=a.split(' ');
	n1=int(l[0]);
	n2=int(l[1])+1;
	num=str(l[0]);
	c=0;
	for i in range(n1,n2):
		num1=num[::-1];
		if num==num1:
			s=str(int(sqrt(int(num))));
			s1=s[::-1];
			#print s
			if s==s1 and str(int(s)*int(s))==num:
				c=c+1
		num=str(int(num)+1)	
	print "Case #"+str(j)+": "+str(c)
#n1=str(int(n1)+1)
#print n1
