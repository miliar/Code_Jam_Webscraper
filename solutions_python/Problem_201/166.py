from collections import defaultdict


def readint():
    return int(input())


def readfloat():
    return float(input())


def readarray(N, foo=input):
    return [foo() for i in range(N)]


def readlinearray(foo=int):
    return list(map(foo, input().split()))


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def gen_primes(max):
    primes = [1] * (max + 1)
    for i in range(2, max + 1):
        if primes[i]:
            for j in range(i + i, max + 1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(2, max + 1) if primes[x]]


def step(a):
    bestl = -1
    bestr = -1
    bestpos = 0
    for i in range(1, len(a) - 1):
        if a[i]:
            continue
        l = 0
        for j in range(i - 1, 0, -1):
            if a[j]:
                break
            else:
                l += 1
        r = 0
        for j in range(i + 1, len(a)):
            if a[j]:
                break
            else:
                r += 1
        if min(bestl, bestr) < min(r, l) or min(bestl, bestr) == min(r, l) and max(bestl, bestr) < max(r, l):
            bestl = l
            bestr = r
            bestpos = i
    a[bestpos] = True
    return bestl, bestr


case_number = readint()
for case in range(case_number):
    N, K = readlinearray()
    d = defaultdict(int)
    d[N] = 1
    last_par = None
    while K > 0:
        # print(d)
        k = max(d.keys())
        K -= d[k]
        d[(k - 1) // 2] += d[k]
        d[k - 1 - (k - 1) // 2] += d[k]
        last_par = k % 2
        del d[k]
    # print(d)
    # exit()
    if last_par:
        l, r = min(d), min(d)
    else:
        l, r = min(d), min(d) + 1
    print("Case #%d: %d %d" % (case + 1, max(l, r), min(l, r), ))
