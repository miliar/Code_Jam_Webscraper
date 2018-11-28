def prog(n,k):
    if(k==1):
        x = ((n+1)/2) - 1
        y = (n-x)-1
        print max(x,y),min(x,y)
    else:
        a = ((n+1)/2) - 1
        b = (n-a)-1
        x = max(a,b)
        y = min(a,b)
        k-=1
        if(k%2 == 0):
            prog(y,k/2)
        else:
            prog(x,(k+1)/2)
t = input()
for T in xrange(1,t+1):
    n,k = map(int,raw_input().split())
    print "Case #"+str(T)+":",
    prog(n,k)
