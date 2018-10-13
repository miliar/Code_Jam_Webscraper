t=int(input())
for t1 in range(1,t+1):
    a,b=raw_input().split()
    a=int(a)
    ans=0
    avail=0
    for i in range(a+1):
        k=ord(b[i])-48
        if i>avail:
            ans+=(i-avail)
            avail+=(i-avail)
        avail+=k
    print 'Case #%d: %d'%(t1,ans)
        
