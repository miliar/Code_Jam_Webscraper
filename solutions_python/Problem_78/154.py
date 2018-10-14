def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

t=int(raw_input())
for ti in range(1,t+1):
    n,pd,pg = [int(i) for i in raw_input().split(' ')[:3]]
    print "Case #%d:"%ti,

    g = gcd(pd,100)
    dde = 100/g
    dno = pd/g

    g = gcd(pg,100)
    gde = 100/g
    gno = pd/g

    f = 1
    if pg == 100 and pd != 100:
        f = 0
    if pg == 0 and pd != 0:
        f = 0

    if dde <= n and f == 1:
        print "Possible"
    else:
        print "Broken"
