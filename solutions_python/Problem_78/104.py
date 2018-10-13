# -*- coding: utf-8 -*-


def gcd(a,b):
	while b>0:
		if a<b:
			b,a = a,b
		a,b = b,a%b
	return a

def proper(n,d):
	if n==0:
		g = d
	else:
		g = gcd(n,d)
	return (n/g,d/g)



T = int(raw_input())

for t in range(1,1+T):
	
	N,pd,pg = [int(w) for w in raw_input().split()]
	wdr,dr = proper(pd,100)
	ldr = dr-wdr
	wgr,gr = proper(pg,100)
	lgr = gr-wgr
	
	pos = (dr<=N) and (wdr==0 or wgr>0) and (ldr==0 or lgr>0)
	
	s = 'Possible' if pos else 'Broken'
	
	print 'Case #{x}: {y}'.format(x=t,y=s)






















