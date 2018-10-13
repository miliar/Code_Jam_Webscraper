t=input()

for q in xrange(t):
    n=input()
    a=map(int,raw_input().split())
    h=a[0]
    l=a[0]
    s=0
    k=0
    m=0
    for i in xrange(1,n):
        if a[i]>=h:
            s=s+h-l
            h=a[i]
            l=a[i]
        elif a[i]>=l:
            s=s+h-l
            h=a[i]
            l=a[i]
        else:
            l=a[i]
    s=s+h-l

    for i in xrange(n-1):
        if a[i]-a[i+1]>m:
            m=a[i]-a[i+1]

    for i in xrange(n-1):
        if a[i]>m:
            k=k+m
        else:
            k=k+a[i]

    print "Case #%d: %d %d" %(q+1,s,k)
