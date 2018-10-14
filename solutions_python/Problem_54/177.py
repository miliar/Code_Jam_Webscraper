def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

ntest=int(raw_input())
for test in range(1,ntest+1):
    buf=raw_input().split(' ')
    n = int(buf[0])
    t=[]
    g = 0
    for i in range(1,n+1):
        y=int(buf[i])
        t.append(y)
        if i!=1:
            if x>y:
                g=gcd(g,x-y)
            else:
                g=gcd(g,y-x)
#        print str(i) + ' ' + str(g)
        x=y
    ans = 0
    for i in range(0,n):
        tmp = t[i] % g
        if tmp==0:
            tmp = 0
        else:
            tmp = g - tmp
        if ans<tmp:
            ans = tmp
    print 'Case #'+str(test)+': '+str(ans)

    
