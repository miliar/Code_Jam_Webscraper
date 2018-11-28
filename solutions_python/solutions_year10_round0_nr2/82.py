import sys

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

C = int(sys.stdin.readline())
for case in xrange(C):
    N, space, t = sys.stdin.readline().partition(' ')
    N = int(N)
    t = [int(x) for x in t.split(' ')]
    
    g = 0
    for ti in t: g = gcd(g, abs(ti-t[0]))

    ret = g - t[0] % g
    if ret == g: ret = 0
    print "Case #{0}: {1}".format(case+1, ret)