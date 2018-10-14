N = long(raw_input())            #number of tests
for x in range(1,N+1):
    r,t=raw_input().split()
    r = long(r)
    t = long(t)
    t1 = t
    y=long(0)
    while True:
        t = t - (2*r +1)
        if t >=0:
            y = y + 1
            r = r + 2
        else:
            break



    print "Case #%d: %d"%(x,y)
    