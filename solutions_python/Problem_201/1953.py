import math

t = int(input())

for i in range(t):
    n,k = map(int,raw_input().strip().split())
    s = int(math.log(k,2))
    s = 2**s
    m = int((n-k)/s)
    if m%2==0:
        mx = m/2
    else:
        mx = m/2+1
    mn = m/2

    print "Case #%d: "%(i+1),mx,mn
