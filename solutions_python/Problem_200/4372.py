t = int(input())
if(t<1 or t>100):
    exit(0)
for p in range(1, t + 1):
    s = int(input())
    d = s
    e = s
    if(s < 1 or s>1000):
        exit(0)


    l = []
    ll = len(l)
    for i in range(1, 5):
        m = int(d % 10)
        l.insert(ll, m)
        d = int(d / 10)



    g = l
    lg = len(g)
    a = l[ll-1] - l[ll - 2]
    b = l[ll-2] - l[ll - 3]
    c = l[ll-3] - l[ll - 4]
    while(c <0 or a<0 or b<0):
        e -= 1
        d = e


        for i in range(0, 4):
            m = int(d % 10)
            g[lg-1-i] = m
            d = int(d / 10)

            a = g[lg - 1] - g[lg - 2]
            b = g[lg - 2] - g[lg - 3]
            c = g[lg - 3] - g[lg - 4]


    print("case #{}: {}".format(p,e))
