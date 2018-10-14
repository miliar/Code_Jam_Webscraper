from sys import *

def solve(i, N, K):
	
	increment = 2**N
	base = 2**N - 1
	
	while(K>base):
		K = K-increment
	
	if K==base:
		print "Case #%d: ON" %(i+1)
	else:
		print "Case #%d: OFF" %(i+1)	

n_cases = int(raw_input())
for i in xrange(n_cases):
	N, K =  map(int, stdin.readline().split())
	
	if(K==0):
		print "Case #%d: OFF" %(i+1)
		continue
	if(N==1 and K==1):
		print "Case #%d: ON" %(i+1)
		continue
		
	solve(i, N, K)