#!/usr/bin/env python 
import sys
###
D_max = 6
P_max = 9
Cut = {}
C= []
for p in xrange(1,P_max+1):
	v = set([ tuple(sorted([i,p-i],reverse=True)) for i in range(1,p) ])
	Cut[p]= sorted(list(v),reverse=False) 

t_minimum = -1
def options(P,t=1,t_min_val=None):
	global t_minimum
	if not t_min_val:
		t_minimum = P_max
	if t > t_minimum:
		return
	q = [ x-1 for x in P ]
	top= max(q)
	if top==0 and t_minimum > t: 
		t_minimum = t
	if top>=0 :
		yield q,t,t_minimum
		for a in options( q, t+1, t_minimum ):  
			yield a
		if P[0]>3:
			for c in Cut[ P[0] ]:
				if c:
					q = sorted( P[1:] + list(c), reverse=True )
					yield q,t,t_minimum
					for a in options( q,t+1, t_minimum ):
						yield a

def solve(D,P):
	P.sort(reverse=True) 
	expected_time = P[0]

	raw= list(P)
	t= P[0]
	for _q,_t,_ in options(P):
		if max(_q)==0 and t>_t:
			t = _t
	y= t
	return y;

def main():

	T = int(input())
	for i in range(1,T+1):
		D = int(sys.stdin.readline())
		P = map(int,sys.stdin.readline().split(' '))
		y = solve(D,P)
		print 'Case #%d: %d'%(i,y)
	return 0

if __name__=='__main__':
	sys.exit(main())
