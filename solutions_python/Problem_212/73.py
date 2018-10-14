def readint():
    return int(input())


def readfloat():
    return float(input())


def readarray(N, foo=input):
    return [foo() for i in range(N)]


def readlinearray(foo=int):
    return list(map(foo, input().split()))


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
    N, P = readlinearray()
    a = readlinearray()
    s = [sum(1 for x in a if x % P == i) for i in range(P)]
    if P == 2:
        answer = s[0] + (s[1] + 1) // 2
    elif P == 3:
        answer = s[0] + min(s[1], s[2])
        l = max(s[1], s[2]) - min(s[1], s[2])
        answer += (l + 2) // 3
    print("Case #%d: %d" % (case + 1, answer))
