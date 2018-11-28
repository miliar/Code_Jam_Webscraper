import os

def test(l,p):
    g = 0
    c = 0
    for x in l:
        if g == 0: c += 1
        g += (x%p)
        g = (g%p)
    return c

def solve2(n,l):
    g = [0,0]
    for x in l:
        g[x%2] += 1
    a,b = g
    r = a + b/2
    if b % 2 == 1: r += 1
    return r

def solve3(n,l):
    g = [0,0,0]
    for x in l:
        g[x%3] += 1
    a,b,c = g
    #print a,b,c
    if b == c:
        return a + b
    if b < c:
        r = a + b + (c-b)/3
        if (c-b) % 3 > 0: r += 1
        return r
    if b > c:
        r = a + (b-c)/3 + c
        if (b-c) % 3 > 0: r += 1
        return r

def solve32(n,l):
    g = [0,0,0]
    for x in l:
        g[x%3] += 1
    a,b,c = g
    t = (max(b,c)-min(b,c))
    r = a + min(b,c) + t/3
    if t % 3 > 0: r += 1
    return r

def solve33(n,l):
    g = [0,0,0]
    ll = [[],[],[]]
    for x in l:
        g[x%3] += 1
        ll[x%3].append(x)
    a,b,c = g
    la,lb,lc = ll
    rl = la
    mi = min(b,c)
    for i in xrange(mi):
        rl.append(lb[i])
        rl.append(lc[i])
    lb = lb[mi:]
    lc = lc[mi:]
    if b > c:
        rl.extend(lb)
    else: rl.extend(lc)

    return test(rl,p)

def solve(n,p,l):
    if p == 2:
        return solve2(n,l)
    if p == 3:
        res = solve3(n,l)
        # res2 = solve33(n, l)
        # print res
        # if res != res2: print "AAAAA", res, res2
        return res
    if p == 4:
        return -1

with open(os.path.expanduser("~/PycharmProjects/gcj/2017/2/A.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        n,p = [int(x) for x in f.readline().strip().split()]
        l = [int(x) for x in f.readline().strip().split()]
        res = solve(n,p,l)
        print 'Case #' + str(i+1) + ': ' + str(res)