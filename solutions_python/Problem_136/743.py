# -- separate project  --BASE FILE for comp-----------
def readint(): return int(f.readline())
def readarray(): return [int(x) for x in f.readline().split()]
def freadarray(): return [float(x) for x in f.readline().split()]

def fun():
	b=2.0;t=0.0;d=0.0
	C,F,X=freadarray()
	while d<X:
		if d==0: t+=C/b;d=C
		if ((X-d)/b)>(X/(b+F)) and d==C:
				d=0;b+=F
		else: 
			t+=(X-d)/b;d=X
			continue
	return t


f=open('in','r');T=readint()
for i in range(1,T+1):
    print "Case #%d: %s" %(i,fun())
