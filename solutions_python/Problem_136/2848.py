from __future__ import division
t=int(raw_input())
for case in xrange(0,t):
    m=map(float,raw_input().split())
    c=m[0]
    f=m[1]
    x=m[2]
    ans=0
    cur=x/2
    den=2+f
    nex=c/2+x/den
    while cur>nex:
	cur=nex
	nex+=x/(den+f)+(c/den)-(x/den)
	den+=f
    den=int((den-2)/f)
    print "Case #%d: %.7f" % (case+1,cur)