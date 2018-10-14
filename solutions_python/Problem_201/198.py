import os

def add(g,n,c):
    if n > 0:
        if n in g:
            g[n] += c
        else:
            g[n] = c

def mm(n):
    if n % 2 == 0:
        return n/2, n/2 - 1
    else:
        return n/2, n/2

def solve(g,k):
    g2 = {}
    s = 0
    for n,c in g.items():
        s += c
        if n % 2 == 1:
            add(g2,n/2, 2*c)
        else:
            add(g2,n/2,c)
            add(g2,n/2 - 1,c)

    if s < k: return solve(g2,k-s)

    a = sorted(g.items(),reverse=True)
    for n,c in a:
        if k <= c:
            return mm(n)
        else:
            k -= c
    print g,a,k



with open(os.path.expanduser("~/PycharmProjects/gcj/2017/qualify/C.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        n,k = [int(x) for x in f.readline().strip().split()]
        if n == k:
            res = (0,0)
        else:
            res = solve({n:1},k)
        print 'Case #' + str(i+1) + ': ' + str(res[0]) + ' ' + str(res[1])