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


case_number = readint()
for case in range(case_number):
    N, C, M = readlinearray()
    ts = readarray(M, readlinearray)
    pos = [[0] * N for i in range(C)]
    for p, b in ts:
        pos[b - 1][p - 1] += 1
    trips = max(sum(x) for x in pos)
    cs = 0
    for i in range(N):
        cs += sum(x[i] for x in pos)
        trips = max(trips, cs // (i + 1) + bool(cs % (i + 1)))
    proms = 0
    for p in range(N):
        proms += max(0, sum(x[p] for x in pos) - trips)
    print("Case #%d: %d %d" % (case + 1, trips, proms))
