floor=[1,1]
for i in range(2,501):
    floor.append(i*floor[-1])

def C(n,m):
    #print n,m
    if m<0:
        return 1
    if m>n:
        return 0
    return (floor[n]/floor[m]/floor[n-m])%100003

anstable={}

def go(c,n):
    if (c,n) in anstable:
        return anstable[(c,n)]
    elif c==1:
        anstable[(c,n)]=1
        return 1
    elif c>=n:
        return 0
    else:
        s=0
        for k in xrange(1, c):
            y=C(n-c-1, c-k-1)
            if y==0:
                continue
            s+=y*go(k,c)%100003

    anstable[(c,n)]=s%100003
    return anstable[(c,n)]

cn=input()
for c in xrange(cn):
    
    x=input()
    s=0
    for i in xrange(1, x):
       s+=go(i,x) 

    
    print "Case #%d: %d" %(c+1, s%100003)
