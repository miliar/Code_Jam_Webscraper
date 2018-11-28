t=int(raw_input())
for cas in xrange(1,t+1):
    c = map(int, raw_input().split())
    d = []
    d.insert(0,c[0])
    while c[1]:
        d=sorted(d)
        i=d.pop()
        if i==1:
            d.insert(0,0)
            d.insert(0,0)
            break
        elif i%2 == 0:
            d.insert(0, i//2)
            d.insert(0, i//2 - 1)
        else:
            d.insert(0, i//2)
            d.insert(0, i//2)
        c[1]-=1
    print "Case #{}: {} {}".format(cas, d[1], d[0])
