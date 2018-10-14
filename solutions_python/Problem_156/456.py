import sys, math
def rs():
    return sys.stdin.readline().strip()
def ri():
    return int(sys.stdin.readline().strip())
def ras():
    return list(sys.stdin.readline().strip())
def rai():
    return map(int,sys.stdin.readline().strip().split())
def raf():
    return map(float,sys.stdin.readline().strip().split())


def solve():
    n = ri()
    arr = rai()
    mx = max(arr)
    res = mx
    for x in xrange(1, mx+1):
        t = 0
        for y in arr:
            if y > x:
                c = int(math.ceil(1.0 * y / x)) - 1
                t += c
        res = min(t+x, res)
    return res



sys.stdout = open('./olb', 'w')
for x in xrange(ri()):
    print "Case #%s: %s"%(x+1, solve())


