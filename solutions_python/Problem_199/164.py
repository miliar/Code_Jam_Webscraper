import string

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
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(2, max+1) if primes[x]]


case_number = readint()
for case in range(case_number):
    s, k = input().split()
    s = list(s)
    k = int(k)
    r = 0
    while '-' in s:
        i = s.index('-')
        if i > len(s) - k:
            print("Case #%d: IMPOSSIBLE" % (case + 1, ))
            break
        s[i : i + k] = ['+' if c == '-' else '-' for c in s[i : i + k]]
        r += 1
    else:
        print("Case #%d: %d" % (case + 1, r))
