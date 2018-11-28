import math
import sys
import time

try: # Use psyco if available
	import psyco
	psyco.full()
except ImportError:
	pass

def pers(a,b,n):
	inner_counter=0
	s=str(n)
	stacka=[]
	for per in xrange(1,len(s)):
		s=s[-1]+s[0:-1]
		#print s
		int_s=int(s)
		if int_s<=b and int_s>=a and int_s>n:
			existence=1
			for v in stacka:
				if v==int_s:
					existence=0
			inner_counter+=existence
			stacka.append(int_s)
	return inner_counter

def main():

	infile = open("C-large.in")
	output = file("output_20120414_2A.txt", 'w')
	infile.readline()
	lrange=infile.readlines()
	lrange=[x.split() for x in lrange]
	print lrange
	lrange=[[int(x[0]),int(x[1])] for x in lrange]
	print lrange
	
	l=0
	for [a,b] in lrange:
		l+=1
		counter=0
		for x in xrange(a,b+1):
			if x<10: continue
			counter+=pers(a,b,x)
		
		print>>output, 'Case #%s:' %l,counter
		
	infile.close()
	output.close()

main()


