T=int(raw_input())
for t in range(1,T+1):
    a=map(int,raw_input().strip().split(' '))
    n=a[0]
    k=a[1]
    import math
    r=int(math.log(k,2))
    r=2**r
    x=int((n-k)/r)
    if(x%2==0):
        print "Case #{}: {} {}".format(t, x/2, x/2)
    else:
        print "Case #{}: {} {}".format(t, x/2+1, x/2)
