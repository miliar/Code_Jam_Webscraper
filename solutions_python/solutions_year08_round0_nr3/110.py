
import sys
import math as m

if len(sys.argv)>1:
  f=open(sys.argv[1],'r').read().split('\n')
else:
  f="""5
0.25 1.0 0.1 0.01 0.5
0.25 1.0 0.1 0.01 0.9
0.00001 10000 0.00001 0.00001 1000
0.4 10000 0.00001 0.00001 700
1 100 1 1 10""".split('\n')
N=int(f[0])
f=f[1:N+1]

def atrig(ax,ay,bx,by,cx,cy):
	A=complex(ax,ay)
	B=complex(bx,by)
	C=complex(cx,cy)
	a=abs(B-C)
	b=abs(A-C)
	c=abs(B-A)
	return m.sqrt((a**2+b**2+c**2)**2-(2*(a**4+b**4+c**4)))/4.0

for case,data in enumerate(f):
	fr,R,t,r,g=map(float,data.split(' '))
	
	r+=fr
	t+=fr
	g-=fr*2.0
	Ri=R-t
	aRi=m.pi*(Ri**2.0)
	aR=m.pi*(R**2.0)	
	a=0.0
	px=r
	
	if g>0 and Ri>0:
		while px<Ri:
			py=r
			while py<(m.sqrt(Ri**2.0-px**2.0)):
				px2=px+g
				py2=py+g
				if abs(complex(px2,py2))<=Ri:
					a+=g*g
				else:
					c1=abs(complex(px2,py))<=Ri
					c2=abs(complex(px,py2))<=Ri
					if c1:
						p1x=px2
						p1y=m.sqrt(Ri**2-px2**2)
					else:
						p1x=m.sqrt(Ri**2-py**2)
						p1y=py
					if c2:
						p2y=py2
						p2x=m.sqrt(Ri**2-py2**2)
					else:
						p2y=m.sqrt(Ri**2-px**2)
						p2x=px
					a+=atrig(px,py,p1x,p1y,p2x,p2y)
					if c1:
						a+=atrig(px,py,p1x,p1y,px2,py)
					if c2:
						a+=atrig(px,py,p2x,p2y,px,py2)
					a+=aRi*(abs(m.atan2(p1x,p1y)-m.atan2(p2x,p2y))/(2*m.pi))-atrig(0.0,0.0,p1x,p1y,p2x,p2y)
					
				py+=g+(2*r)
			px+=g+(2*r)
			
	prob=1-((a*4)/aR)
	
	print "Case #%i: %f"%(case+1,prob)




