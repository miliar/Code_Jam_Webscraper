#!/usr/bin/python
import sys

def nextLine():
	return sys.stdin.next()[:-1]

def debug(s):
	sys.stderr.write("# "+s+"\n")


def process(A):
	count = 0
	while True:
#print A,count
		p =  -1
		for i in xrange(len(A)):
			if A[i] > i+1:
				p = i
				break
		if p == -1:
			return count
		if A[p+1] <= p +1:
			A[p],A[p+1] = A[p+1],A[p]
			count += 1
		else:
			for i in xrange(p+1,len(A)):
				if i+1 > A[i] and A[i-1] > A[i] and A[i] <=p+1:
					A[i],A[i-1] = A[i-1],A[i]
					count += 1
					break;

N = int(nextLine())
for c in range(N):
	total = 0
	size = int(nextLine())
	M =[]
	for i in range(size):
		input = nextLine()
		p = input.rfind("1")+1;
		M.append(p)
	total = process(M)

	print "Case #%d: %d"%(c+1,total)

