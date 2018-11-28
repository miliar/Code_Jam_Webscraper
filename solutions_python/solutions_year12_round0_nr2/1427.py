from math import floor

def isp(t, p):
    # -1 : impossible
    #  0 : surprising
    #  1 : possible
    if t == 0 and p == 1:
        return -1
    if t < 3*p - 4:
        return -1
    if t < 3*p - 2:
        return 0
    return 1

T = int(raw_input())
for case in xrange(T):
    line = map(int, raw_input().split())
    N = line[0]
    S = line[1]
    p = line[2]
    t = line[3:]
    r = map(lambda x: isp(x, p), t)
    n = r.count(1) + min(r.count(0), S)
    print "Case #%i: %i" % (case+1, n)
