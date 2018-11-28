import sys
from decimal import *

sys.stdin = open('B-small-attempt0.in')
sys.stdout = open('out.txt', 'w')

N = 10**12
eps = 10**-8

n_cases = int(input())
for case in range(n_cases):
    print(case, end=' ', file=sys.stderr)
    w = input().split()
    n, v, x  = int(w[0]), float(w[1]), float(w[2])
    sr = [''] * n; sc = ['']*n
    r = [0] * n; c = [0]*n
    l = []; m = []; u = []
    for i in range(n):
        sr[i], sc[i] = input().split()
        if Decimal(sc[i]) < Decimal(w[2]):
            l.append(i)
        if Decimal(sc[i]) == Decimal(w[2]):
            m.append(i)
        if Decimal(sc[i]) > Decimal(w[2]):
            u.append(i)
        r[i], c[i] = float(sr[i]), float(sc[i])

    nl = len(l)
    for i in range(nl):
        for j in range(i+1, nl):
            if c[l[i]] > c[l[j]]:
                l[i],l[j] = l[j], l[i]
    nu = len(u)
    for i in range(nu):
        for j in range(i+1, nu):
            if c[u[i]] > c[u[j]]:
                u[i],u[j] = u[j], u[i]
    nm = len(m)


    if m==[] and (l==[] or u==[]):
        res = 'IMPOSSIBLE'
    else:

        sum_l = sum([r[i]*c[i] for i in l])
        sum_m = sum([r[i]*c[i] for i in m])
        sum_u = sum([r[i]*c[i] for i in u])
        sum_target = sum([r[i]*x for i in l+u])

        l_bottleneck = sum_l + sum_u > sum_target
        res = 0
        a=0; b = 10**10

        while b-a > eps:
            t = a + 0.5 * (b-a)
            ok = True
            if l_bottleneck:
                vol = [0] * n
                for i in range(nl):
                    vol[l[i]] = t * r[l[i]]
                for i in range(nm):
                    vol[m[i]] = t * r[m[i]]
                for i in range(nu):
                    lhs = sum([vol[j]*c[j] for j in range(n)])
                    rhs = sum([vol[j]*x for j in range(n)])
                    if lhs < rhs:
                        if lhs + t * r[u[i]] * c[u[i]] < rhs + t * r[u[i]] * x:
                            vol[u[i]] = t * r[u[i]]
                        else:
                            vol[u[i]] = (rhs - lhs) / (c[u[i]] - x)
                ok = sum(vol) >= v
            else:
                vol = [0] * n
                for i in range(nm):
                    vol[m[i]] = t * r[m[i]]
                for i in range(nu):
                    vol[u[i]] = t * r[u[i]]

                for i in range(nl-1, -1,-1):
                    lhs = sum([vol[j]*c[j] for j in range(n)])
                    rhs = sum([vol[j]*x for j in range(n)])
                    if lhs > rhs:
                        if lhs + t * r[l[i]] * c[l[i]] > rhs + t * r[l[i]] * x:
                            vol[l[i]] = t * r[l[i]]
                        else:
                            vol[l[i]] = (lhs - rhs) / (x - c[l[i]])
                ok = sum(vol) >= v

            if ok:
                b = t
            else:
                a = t

        res = t
    print('Case #{}: {}'.format(case+1, res))

print(file=sys.stderr)

