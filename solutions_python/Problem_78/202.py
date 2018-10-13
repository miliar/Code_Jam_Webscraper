def gcd(a,b):
    if a==0: return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)/gcd(a,b)

t=int(raw_input())
for tt in range(t):
    n,pd,pg=map(int,raw_input().split())
    md=gcd(pd,100)
    #ag=100/gcd(pg,100)
    #print ad
    if 100/md<=n and (pg!=100 or pd==100) and (pg!=0 or pd==0):
        print "Case #%d: Possible"%(tt+1)
    else:
        print "Case #%d: Broken"%(tt+1)
