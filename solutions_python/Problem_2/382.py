#!/usr/bin/python

n = int(raw_input())
for i in range(1, n+1):
    t = int(raw_input())
    na, nb = raw_input().split(" ")
    na=int(na)
    nb=int(nb)
    
    asub=[]
    aadd=[]
    bsub=[]
    badd=[]
    for j in range(na):
        d, a = raw_input().split(" ")
        d=int(d.split(":")[0])*60 + int(d.split(":")[1])
        a=int(a.split(":")[0])*60 + int(a.split(":")[1])
        asub.append(d)
        badd.append(a+t)
    for j in range(nb):
        d, a = raw_input().split(" ")
        d=int(d.split(":")[0])*60 + int(d.split(":")[1])
        a=int(a.split(":")[0])*60 + int(a.split(":")[1])
        bsub.append(d)
        aadd.append(a+t)
        
    numa=0
    numb=0
    mina=0
    minb=0
    for k in xrange(0, 1440):
        if k in asub: numa -=asub.count(k)
        if k in aadd: numa +=aadd.count(k)
        if k in bsub: numb -=bsub.count(k)
        if k in badd: numb +=badd.count(k)
        
        if numa<mina: mina=numa
        if numb<minb: minb=numb
        
    print "Case #%i: %i %i" % (i, -mina, -minb)
    