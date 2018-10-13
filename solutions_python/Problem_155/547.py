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
    a,b = sys.stdin.readline().strip().split(" ")
    arr = map(int,list(b))
    mx = int(a)
    if mx == 0: return 0
    count = 0
    r = 0
    for x in xrange(mx+1):
        if x > count:
            r += x - count
            count = x
        count += arr[x]
    return r


for x in xrange(ri()):
    print "Case #%s: %s"%(x+1, solve())


