import os

def solve(d,n,l):
    ma = 0
    gk = l[0][0]
    gs = l[0][1]
    for k,s in l:
        if s*(d-gk) < gs*(d-k):
            ma = 1.*(d-k)/s
            gk = k
            gs = s
    return 1.*d*gs/(d-gk)

with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1B/A.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        d,n = [int(x) for x in f.readline().strip().split()]
        l = []
        for j in xrange(n):
            k,s = [int(x) for x in f.readline().strip().split()]
            l.append((k,s))
        res = solve(d,n,l)
        print 'Case #' + str(i+1) + ': ' + str(res)