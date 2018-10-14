#!/usr/bin/python
import math
import sys

#This is my first python program
#it's ugly, I know


def pal(num):
	original=num
	revered=0
	while original >0 :
		revered=revered*10 + original % 10
		original=original/10
	return revered == num


def check_far_sqaure(a,b):
	count=0
	a_lower=int(math.sqrt(a))-1
	b_lower=int(math.sqrt(b))+1
	for x in range(a_lower, b_lower):
		tmp=x*x
		if pal(x) and pal(tmp) and a<=tmp<=b:
			count+=1
	print count

f=open('in.test',"r")
line=f.readline()
cases=int(line)
line=f.readline()
for i in range(1, cases+1):
	sys.stdout.write("Case #%s: " % i)
	a,b=line.split()
	a,b=[int(a) , int(b)]
	check_far_sqaure(a,b)
	line=f.readline()

f.close()