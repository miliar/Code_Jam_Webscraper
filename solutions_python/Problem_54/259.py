def euclid(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

t = int(raw_input())

for i in xrange(1,t+1):
    y = [long(x) for x in raw_input().split()][1:]    
    n = len(y)
    x = []
    for j in xrange(1,n):
        x.append(abs(y[0]-y[j]))

    if n==2:
        m=x[0]
    else:
        m=x[0]
        for j in xrange(1,n-1):
            m=euclid(m,x[j])

    print "Case #%d: %d"%(i,(m-y[0]%m)%m)
