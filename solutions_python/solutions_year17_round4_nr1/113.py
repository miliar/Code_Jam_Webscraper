# usage:  (python3 a.py < a.in) > a.out
import time, sys, inspect

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)

#---------------------------------------------

'''
how many get
    1 + num(Gi is mul of P) + num(multiple Gi make multiple of P)
'''

def run(data):
    p, data = data
    data = [d%p for d in data]
    print(data)

    if p == 2:
        # -1//2 = -1  but ok
        return 1 + data.count(0) + (data.count(1)-1)//2

    if p == 3:
        match0 = min(1 + data.count(0), len(data))
        n1 = data.count(1)
        n2 = data.count(2)
        min12 = min(n1, n2)
        match12 = max(min12 - (1 if n1 == n2 else 0), 0)
        n1 -= min12
        n2 -= min12
        match111 = max((n1-1)//3, 0)
        match222 = max((n2-1)//3, 0)
        print(match111, match12, match222)
        return match0 + match12 + match111 + match222

    if p == 4:
        match0 = min(1 + data.count(0), len(data))
        n1 = data.count(1)
        n2 = data.count(2)
        n3 = data.count(3)
        #
        min13 = min(n1, n3)
        match13 = max(min13 - (1 if n1 == n3 and n2 == 0 else 0), 0)
        n1 -= min13
        n3 -= min13
        match22 = max(n2//2 - (1 if n2%2 == 0 and n1 == n3 == 0 else 0), 0)
        n2 %= 2
        #
        min112 = min(n1//2, n2)
        min332 = min(n3//2, n2)
        # only one of [n1,n3] nonzero so ok
        match112 = max(min112 - (1 if 2*min112 == n1 and min112 == n2 else 0), 0)
        match332 = max(min332 - (1 if 2*min332 == n3 and min332 == n2 else 0), 0)
        n1 -= 2*match112
        n3 -= 2*match332
        n2 -= match112 + match332
        #
        match1111 = max((n1-1)//4, 0)  # only one of these nonzero so ok
        match3333 = max((n3-1)//4, 0)
        ret = [match0, match13, match22, match112, match332, match1111, match3333]
        print(ret)
        return sum(ret)


import itertools, random

def bf_sol(data):
    p, a = data
    print(data)
    maxi = 0
    for m in itertools.permutations(a):
        pp = [None] * (len(m)-1)
        tot = 0
        for i in range(len(m)-1):
            tot += m[i]
            tot %= p
            pp[i] = tot
        maxi = max(maxi, pp.count(0))
        # print(m, pp, pp.count(0))
    return 1+maxi

def test():
    for l in range(1, 10):
        for _ in range(20):
            a = [random.randint(0, 3) for _ in range(l)]
            print(a)
            print(bf_sol([4, a]), run([4, a]))
            assert bf_sol([4, a]) == run([4, a])

#---------------------------------------------

def read_case():
    n, p = [int(k) for k in list(input().split())]
    return (p, [int(k) for k in list(input().split())])

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
