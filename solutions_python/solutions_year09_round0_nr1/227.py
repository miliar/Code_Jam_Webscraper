l,d,n=map(int,raw_input().split())
words=[]
for x in xrange(d):
    words.append(raw_input())
for x in xrange(n):
    pos=[]
    t=list(raw_input())
    i=0
    sub=False
    while i<l:
        sl=t.pop(0)
        if sl=="(":
            tmp=[]
            sub=True
            continue
        if sl==")":
            pos.append(tmp)
            i+=1
            sub=False
            continue
        if sub:
            tmp.append(sl)
        else:
            pos.append([sl])
            i+=1
    match=0
    for i in words:
        ok=True
        for p,w in enumerate(i):
            if not w in pos[p]:
                ok=False
        if ok:
            match+=1
    print "Case #%i: %i"%(x+1,match)
