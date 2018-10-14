#!/usr/bin/python
import sys

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

def main():
	[T]=read_ints()
	for t in xrange(1,T+1):
		[N,M]=read_ints()
		reqd=0
		d={('',):0}
		n=1
		while n<=N:
			direct = tuple(raw_input().split('/'))
			for i in xrange(1,len(direct)+1):
				x=direct[0:i]
				if x not in d:
					d[x] = len(x)
			n+=1
		m=1
		while m<=M:
			direct = tuple(raw_input().split('/'))
			for i in xrange(1,len(direct)+1):
				x=direct[0:i]
				if x not in d:
					reqd+=1
					d[x] = len(x)
			m+=1
		print "Case #%d: %d" % (t,reqd)


if __name__=='__main__':
	main()

