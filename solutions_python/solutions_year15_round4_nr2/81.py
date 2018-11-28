ttt = int(raw_input())
for tt in xrange(1, ttt+1):
    def makeint(f):
        return int((float(f)*10000)+0.0001)
    inp = raw_input().strip().split()
    n = int(inp[0])
    vv = makeint(inp[1])
    xx = makeint(inp[2])
    r = [0] * n
    x = [0] * n
    for i in xrange(n):
        r[i], x[i] = map(makeint, raw_input().strip().split())
    fail = False
    ans = 0
    if n == 1:
        if x[0] != xx:
            fail = True
        else:
            ans = float(vv)/r[0]
    elif n == 2:
        if x[0] == x[1]:
            if x[0] != xx:
                fail = True
            else:
                ans = float(vv)/(r[0]+r[1])
        else:
            v0 = float((xx-x[1])*vv)/(x[0]-x[1])
            v1 = float((xx-x[0])*vv)/(x[1]-x[0])
            if v0 < 0 or v1 < 0:
                fail = True
            else:
                ans = max(v0/r[0], v1/r[1])

    else:
        # give up
        fail = True
    if fail:
        print 'Case #%d: IMPOSSIBLE' % tt
    else:
        print 'Case #%d: %f' % (tt, ans)