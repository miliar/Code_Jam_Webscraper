#!/usr/bin/env python
from sys import stdin

T = int(stdin.readline())
	
def rotate(n,length):
	return n/10 + (n%10)*pow(10,length-1)
# 
# def check_valid(n, m, length):
# 	for i in xrange(0,length-1):
# 		m = rotate(m,length)
# 		if m == n: return
# 	print "ERROR!"
# 	

for i in xrange(T):
	
	A,B = map(int, stdin.readline().split(" "))
	l = len(str(A))
	count = 0
		
	for n in xrange(A, B+1):
		
		m = n
		found = {}
		
		for rot in xrange(1,l):
			
			m = rotate(m,l)
			if m > n and m <= B and not (n,m) in found: 
				count += 1
				found[(n,m)] = True
				#print "A:%d B:%d n:%d m:%d v"% (A,B,n,m)
				#check_valid(n,m,l)
				#newpair = "%d-%d" % (n, m)
				#if newpair in list:
				#	print "FAULT!"
				#else : list.append(newpair)
				
				
				
			#else:	print "A:%d B:%d n:%d m:%d"% (A,B,n,m)
			
		
	print "Case #%d: %d" % (i+1, count)
