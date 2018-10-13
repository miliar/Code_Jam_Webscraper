import os
import sys

f = open(sys.argv[1]).readlines()

testCases = int(f[0])
j = 0

def check(alist,flag):
	if len(alist)>1:
       		mid = len(alist)//2
      		lefthalf = alist[:mid]
	        righthalf = alist[mid:]
		if int(alist[0])<=int(alist[mid]) and int(alist[len(alist)-1])>=int(alist[mid]):
	        	l = check(lefthalf, flag)
	  	 	r = check(righthalf, flag)
			return 1
		else:
#			print "Wrong",alist[0],alist[mid],alist[len(alist)-1]
#			print "Wrong",alist[:mid],alist[mid:]
#			flag = 0
			return 0

for i in range(testCases):
	j+=1
	num = int(f[j])
	z = num	
	while(z > 0):
		if len(str(z))==1:
			print "Case #"+str(i+1)+": "+str(z)
			break
		else:
			if check(str(z),1)==1:
				print "Case #"+str(i+1)+": "+str(z)
				break		
		z=z-1	

