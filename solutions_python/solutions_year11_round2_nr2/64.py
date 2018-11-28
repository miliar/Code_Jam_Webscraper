import sys

def possible(t):
	p=pts[0]-t
	for i in range(1,L):
		if abs(pts[i]+t-p)<D: return False
		if p+D<pts[i]:
			if pts[i]-t>p+D:
				p=pts[i]-t
			else:
				p=p+D
		else:
			p=p+D
	return True

eps=1e-7
T = int(sys.stdin.readline().strip())
	
for t in range(1,T+1):
	C,D =map(int,sys.stdin.readline().strip().split(' '))
	pts=[]
	for i in range(C):
		p,v=map(int,sys.stdin.readline().strip().split(' '))
		for j in range(v): pts.append(p)
	L=len(pts)
	lo=0.0
	hi=500001
	while abs(hi-lo)>eps:
		mid = (lo+hi)/2
		if possible(mid):
			hi=mid
		else:
			lo=mid
	if L==1:
		print 'Case #%d: 0' % t
	else:
		print 'Case #%d: %s' %(t,str(lo))
