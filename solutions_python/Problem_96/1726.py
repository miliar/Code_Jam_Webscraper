import sys

def solve(N, S, p, ts):
    N, S, p = map(int, [N, S, p])
    #print N, S, p, ts

    ss = S
    cnt = 0

    for t in ts:
        if t == 0:
            if p == 0:
                cnt += 1
            continue
#        print "t: %d" % t
        c = t / 3
        r = t % 3
#        print c, r
        if c >= p:
            cnt += 1
            continue
        if r == 0:
            if ss > 0 and t > 1 and c + 1 >= p:
                ss = ss - 1
                cnt += 1
                continue
        if r == 1:
            if c + 1 >= p:
                cnt += 1
                continue
        if r == 2:
            if c + 1 >= p:
                cnt += 1
                continue
            if ss > 0 and c + 2 >= p:
                ss = ss - 1
                cnt += 1
                continue
 #       print "NO"

    return cnt


for i in xrange(int(raw_input())):
    N, S, p, ts = sys.stdin.readline().strip().split(' ', 3)
    ts = map(int, ts.split(' '))
    print 'Case #%d: %d' % (i+1, solve(N, S, p, ts))
