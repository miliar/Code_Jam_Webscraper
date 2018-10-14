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


def solve(x,r,c):
    s = r*c
    ch = s / x
    mn = min(r,c)
    mx = max(r,c)
    if ch*x != s or mn+mn+1 <= x or x > mx or (x==4 and mx==4 and mn==2): return "RICHARD"
    else: return "GABRIEL"


sys.stdout = open('./osd', 'w')
for i in xrange(ri()):
    x,r,c = rai()
    print "Case #%s: %s"%(i+1, solve(x,r,c))

# for x in xrange(1,5):
#     for c in xrange(1,5):
#         for r in xrange(1, c+1):
#             print x,r,c, solve(x,r,c)