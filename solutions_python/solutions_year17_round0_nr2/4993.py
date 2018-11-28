
t=input()
for ii in xrange(0,t):
    n=input()
    while n>=1:
        k=str(n)
        l=len(k)
        c=1
        for i in xrange(0,l-1):
            a=int(k[i])
            b=int(k[i+1])
            if a>b:
                break
            c+=1
        if c==l:
            break
        n-=1
    print 'Case #'+str(ii+1)+':',n
        
