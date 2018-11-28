cases=int(raw_input())
for z in xrange(cases):
    n=int(raw_input())
    l=map(int,raw_input().split())
    a=0
    j=l[0]
    for k in l:
        if k<=j:
            a+=(j-k)
            j=k
        else:
            j=k
    b=0
    x=max([l[i-1]-l[i] for i in xrange(1,n)])
    for i in xrange(n-1):
        if l[i]<=x:
            b+=l[i]
        else:
            b+=x
    print 'Case #'+str(z+1)+': '+str(a)+' '+str(b)
