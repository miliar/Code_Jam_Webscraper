cases=int(raw_input())
for c in xrange(cases):
    n,l=raw_input().split()
    l=map(int,list(l))
    n=int(n)
    coun=0
    req=0
    for i in xrange(n+1):
        if i<=coun:
            coun+=l[i]
            continue
        else:
            req+=(i-coun)
            coun=i+l[i]
    print 'Case #'+str(c+1)+': '+str(req)
