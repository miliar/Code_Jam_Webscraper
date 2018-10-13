import math
t=input()
for x in xrange(0,t):
    l=raw_input()
    p={}
    for y in xrange(0,len(l)):
        if l[y] not in p: p[l[y]]=y
    b=len(p)
    if b==1: 
        print "Case #%d: %d" % (x+1, (2**len(l))-1)
    else:
        i=p.items()
        i.sort(key=lambda x:x[1])
        h=map(lambda x:x[0],i)
        tmp=h[0]
        h[0]=h[1]
        h[1]=tmp
        digits={}
        for q in xrange(0,b): digits[h[q]]=q
        n=0
        for y in l:
            n*=b
            n+=digits[y]
        print "Case #%d: %d" % (x+1, n)


