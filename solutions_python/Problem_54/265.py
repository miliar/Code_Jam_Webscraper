#! /usr/bin/python

from sys import stdin

def gcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a

def list_gcd(lst):
	return reduce(lambda x,y: gcd(x,y),lst[2:],gcd(lst[0],lst[1]))
	
def compute(numbers):
	candidates=[abs(a-b) for i,a in enumerate(numbers) for j,b in enumerate(numbers) if i<j]
	if len(candidates)>1:
		T=list_gcd(candidates)
	else:
		T=candidates[0]
	
	if numbers[0]%T:
		return T-numbers[0]%T
	else:
		return 0
	
if __name__=='__main__':
	C=int(stdin.readline())
	for case in xrange(1,C+1):
		numbers=map(int,stdin.readline().split())[1:]
		print "Case #%d: %d"%(case, compute(numbers))
