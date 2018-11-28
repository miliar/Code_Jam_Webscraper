t=int(input())
for tt in range(t):
    n=int(input())
    c=raw_input()
    c=c.split(" ")
    c=map(int,c)
    
    r=0
    s=0
    m=c[0]
    for x in c:
        r=r^x
        s+=x
        m=min(x,m)
    if r==0:
        print "Case #%d: %d"%(tt+1,s-m)
    else:
        print "Case #%d: NO"%(tt+1)
