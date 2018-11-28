#!/usr/bin/python
import math


def solve(case):
    howmany=0
    for i in range(case[0],case[1]+1):
        if str(i)==str(i)[::-1]:
	    sqr=math.sqrt(i)
	    if str(sqr)[-2:]=='.0':
	      sqr=int(sqr)
	    else:
	      pass
	    if str(sqr)==str(sqr)[::-1]:
		howmany+=1
    return howmany

f=open('/tmp/case3')
num=int(f.readline())
#print num
for i in range(1,num+1):
   #
   print "Case #" + str(int(i))+":",solve(map(int,f.readline().split(" ")))