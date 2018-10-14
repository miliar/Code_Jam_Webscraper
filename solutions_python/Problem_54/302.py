def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

t=input()
o=t
t=t-1
while t>=0:
    haha=map(int,raw_input().split())
    n=haha[0]
    a=haha[1:]
    a.sort()
    b=[]    
    for i in range(0,n-1,1):
        b.append(a[i+1]-a[i])
    if n==2:
        ans = a[0]%b[0]
        if ans!=0:
            ans=b[0]-ans
        print 'Case #%(0)s: %(1)s'%{'0':str(o-t),'1':str(ans)}
    else:
        g=gcd(b[0],b[1])
        for i in range(2,n-1,1):
            g=gcd(g,b[i])
        ans=a[0]%g
        if ans!=0:
            ans=g-ans
        print 'Case #%(0)s: %(1)s'%{'0':str(o-t),'1':str(ans)}
    t=t-1
