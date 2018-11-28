import sys

def doit():
    pass

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b % a, a)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    d = {'O':0, 'B':1}
    for _t in xrange(t):
        t, pd, pg = map(int, f.readline().split())

        gd = gcd(pd, 100)
        won_today = pd / gd
        played_today = 100 / gd
        if played_today > t or (pg == 0 and pd != 0) or (pg == 100 and pd != 100):
            print "Case #%d: Broken" % (_t+1)
            continue
        else:
            print "Case #%d: Possible" % (_t+1)


