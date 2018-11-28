import sys

dic = None
cs = None
vs = None
p = 0
n = 0

INF = 10**10
def ticket(r, k, c):
    if (r,k,c) in dic:
        return dic[(r,k,c)]
    if(r == p):
        if c <= cs[k]:
            res = 0
        else:
            res = INF
    else:
        res1 = ticket(r+1, 2*k, c) + ticket(r+1, 2*k+1, c) + vs[r][k]
        res2 = ticket(r+1, 2*k, c+1) + ticket(r+1, 2*k+1, c+1)
        res = min(res1,res2)
    dic[(r,k,c)] = res
    return res

t = int(sys.stdin.readline())
for _ in range(1,t+1):
    p = int(sys.stdin.readline())
    n = (1<<p)
    cs = [int(x) for x in sys.stdin.readline().split()]
    vs = [list() for i in range(p)]
    for i in range(p):
        vs[p-1-i] = [int(x) for x in sys.stdin.readline().split()]
    dic = dict()
    res = ticket(0, 0, 0)
    print 'Case #%d: %d' % (_, res)
