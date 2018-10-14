
scores = []
def xset(t):
    data = (t[0], sum(t), t[0] - t[-1] > 1)
    scores.append(data)
    #print t, data
for x in xrange(11):
    xset((x,x,x))
    if x > 0:
        xset((x,x,x-1))
        xset((x,x-1,x-1))
    if x > 1:
        xset((x,x,x-2))
        xset((x,x-1,x-2))
        xset((x,x-2,x-2))

AP, AS = {}, {}
for mx in xrange(11):
    AP[mx] = set(x[1] for x in scores if x[0] >= mx and not x[2])
    AS[mx] = set(x[1] for x in scores if x[0] >= mx and x[2])

def solve(N, S, p, t):
    cpass, csurp = 0, 0
    for v in t:
        if v in AP[p]:
            cpass += 1
        elif v in AS[p]:
            csurp += 1
    return cpass + min(csurp, S)

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        data = f.readline().split(' ')
        N, S, p = map(int, data[:3])
        t = map(int, data[3:])
        assert len(t) == N
        res = solve(N, S, p, t)
        print 'Case #%d: %d' % (i + 1, res)

if __name__ == '__main__':
    import sys
    main(sys.stdin)
