#!/usr/bin/python
import sys

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

def main():
	[C]=read_ints()
	for c in xrange(1,C+1):
		[N,K,B,T]=read_ints()
		op=read_ints()
		ov=read_ints()
		mint=list(op)
		maxk=0
		for i in xrange(0,len(op)):
			mint[i]= (B-op[i])/ov[i]
			if (B-(mint[i]*ov[i]+op[i]) > 0): mint[i]+=1
			if mint[i] <= T: maxk+=1
		if maxk >= K:
			reqs=0
			k=0
			sol=0
			for i in xrange(len(op)-1,-1,-1):
				if(op[i] >= B): k+=1
			if(k>=K): sol=1
			while sol == 0:
				#print mint
				minti = 0
				for i in xrange(len(op)-k-1,-1,-1):
					if(mint[i] <= T):
						minti = i
						#print i
						break
				if minti < len(op)-k-1:
					reqs +=len(op)-k-1 - minti 
					temp = mint[minti]
					for i in xrange(minti, len(op)-k-1):
						mint[i] = mint[i+1]
					mint[len(op)-k-1] = temp
				k+=1
				#print k
				if(k>=K): sol=1
			print "Case #%d: %d" % (c,reqs)
		else: print "Case #%d: IMPOSSIBLE" % (c)

if __name__=='__main__':
	main()

