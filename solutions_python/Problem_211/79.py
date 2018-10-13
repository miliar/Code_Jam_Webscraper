import os
from decimal import Decimal, getcontext

getcontext().prec = 20

g = 10000
de8 = Decimal(10) ** -8

# def solve2(n,k,u,l):
#     l = sorted(l)
#     if n * g - sum(l) <= u: return Decimal(1).quantize(de8)
#     l.append(g)
#     c = 0
#     for i in xrange(n):
#         if u == 0: break
#         t = l[i+1]
#         x = l[i]
#         c += 1
#         if u >= c * (t - x):
#             u = u - c * (t - x)
#             for j in xrange(c):
#                 l[j] = t
#         else:
#             d = u/c
#             for j in xrange(c):
#                 l[j] += d
#             for j in xrange(u - c * d):
#                 l[j] += 1
#             u = 0
#
#     pp = 1
#     for x in l[:-1]:
#         pp *= x
#     r = Decimal(pp)
#     r = r/Decimal(g**n)
#     if r < Decimal(10)**(-8):
#         return 0.00000000
#     return r.quantize(de8)

def solve(n,k,u,l):
    l = sorted(l)
    l.append(g)
    c = 0
    for i in xrange(n):
        t = l[i+1]
        x = l[i]
        c += 1
        if u >= c * (t - x):
            u = u - c * (t - x)
            for j in xrange(c):
                l[j] = t
        else:
            d = u/c
            for j in xrange(c):
                l[j] += d
            for j in xrange(u - c * d):
                l[j] += 1
            u = 0

    pp = 1
    for x in l[:-1]:
        pp *= x
    r = Decimal(pp)
    r = r/Decimal(g**n)
    if r < Decimal(10)**(-8):
        return 0.0
    return r.quantize(de8)

with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1C/C.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        n,k = [int(x) for x in f.readline().strip().split()]
        u1,u2 = [int(x) for x in f.readline().strip().split('.')]
        u = u1*g + u2
        l = []
        for xx in f.readline().strip().split():
            p1,p2 = [int(x) for x in xx.split('.')]
            l.append(p1*g + p2)
        res = solve(n,k,u,l)
        print 'Case #' + str(i+1) + ': ' + str(res)