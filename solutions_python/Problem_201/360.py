import math

def solve(n,k):
    p = k
    b = 0
    a = n

    while(p>1):
        p/=2
        a-=1
        a = int(math.ceil(float(a)/2))
        b+=1

    # print a,b

    l = (1<<b)
    x = (n-l+1)-(l*(a-1))

    # print x,a,l

    p = k-l+1
    a-=1

    if(p<=x):
        if(a%2==0): return a/2,a/2
        else: return a/2+1,a/2
    else:
        a-=1
        if(a%2==0): return a/2,a/2
        else: return a/2+1,a/2


t = int(raw_input())

for i in range(1,t+1):
    n,k = map(int,raw_input().strip().split(' '))
    x,y = solve(n,k)
    print "Case #%d: %d %d" %(i,x,y)
