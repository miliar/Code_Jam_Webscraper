def cry(st):
    global v
    x1,x2 = 0,0
    s = 0
    for i in range(len(v)):
        if st & (1<<i):
            x1 ^= v[i]
            s += v[i]
        else:
            x2 ^= v[i]
    if x1 == x2:
        return s
    else:
        return -1

t = int(raw_input())
for ti in range(1, t+1):
    print "Case #%d:" % ti,

    n = int(raw_input())
    v = [int(i) for i in raw_input().split(' ')[:n]]

    r = -1
    for i in range(1, (1<<n)-1):
        cr = cry(i)
        if r < cr:
           r = cr
    if r < 0:
        print 'NO'
    else:
        print r
