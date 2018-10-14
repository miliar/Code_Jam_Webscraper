import sys
fi = open(sys.argv[1])
fo = open(sys.argv[2], 'w')
fr = fi.readline

T = int(fr())
for t in xrange(T):
    tmp = map(int, fr().split())
    N, S, p = tmp[:3]
    tt = tmp[3:]
    tt.sort(reverse=True)
    res = 0
    for i in tt:
        if (i+2)/3 >= p:
            res += 1
        elif i <= 2:
            if i >= p and S != 0:
                S -= 1
                res += 1
        elif (i+4)/3 >= p:
            if S != 0:
                S -= 1
                res += 1
        else:
            break
    fo.write("Case #%d: %d\n" % (t+1, res))
fo.close()
