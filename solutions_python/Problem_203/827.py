from itertools import *
import math 
import sys

#sys.stdout = open('op.txt', 'w')


t = input()
for case in xrange(1,t+1):
	ip = raw_input()
	r,c=ip.split()
	r=int(r);c=int(c)
	if r==2 and c==2:
		ans=4
	elif r==2 :
		ans=(r*c)-((c/3)*r)
	elif c==2:
		ans=(r*c)-((r/3)*c)
	elif r%2==0:
		li  = [0]*((r+1)*c)
		cnt=0
		for x in xrange(len(li)):
			if cnt==1 or cnt ==0:
				li[x]=1
				cnt+=1
			else:
				cnt=0
		#print li
		temp = 0
		x=r
		while x<len(li):
			#print x,li[x],temp
			temp+=li[x]
			x+=r+1

		ans =sum(li)-(temp)
	else:
		li = [0]*(r*c)
		cnt=0
		for x in xrange(len(li)):
			if cnt==1 or cnt ==0:
				li[x]=1
				cnt+=1
			else:
				cnt=0
		#print li
		
		ans= sum(li)



	print "Case #%d: %d"%(case,ans)
