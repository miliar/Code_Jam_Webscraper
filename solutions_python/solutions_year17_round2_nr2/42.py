from re import *
from sys import stderr
def readint():
    return int(input())
def readfloat():
    return float(input())
def readarray(N, foo=input):
    return [foo() for i in range(N)]
def readlinearray(foo=int):
    return map(foo, input().split())

def NOD(a, b):
    while b:
        a,b = b, a%b
    return a

def gen_primes(max):
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(max+1) if primes[x]]

def is_prime(N):
    i = 3
    if not(N % 2):
        return 0
    while i*i < N:
        if not(N % i):
            return 0
        i += 3
    return 1

case_number = readint()
for case in range(case_number):
    N, R, O, Y, G, B, V = readlinearray()
    r = R - G
    y = Y - V
    b = B - O
    if max(r, y, b) * 2 > r + y + b:
        print("Case #%s: %s" % (case + 1, "IMPOSSIBLE", ))
        continue
    if r == 0 and y == 0 and b == 0:
        if sum(map(bool, [R, O, Y, G, B, V])) > 2:
            print("Case #%s: %s" % (case + 1, "IMPOSSIBLE", ))
            continue
        else:
            s = "RG" * R + "YV" * Y + "BO" * B
    else:
        s = ""
        data = [["R", r], ["Y", y], ["B", b]]
        # print(data)
        data.sort(key=lambda x: x[1], reverse=True)
        while data[0][1] > 0:
            s += data[0][0]
            data[0][1] -= 1
            t = 1 if data[1][1] >= data[2][1] else 2
            s += data[t][0]
            data[t][1] -= 1
        assert(abs(data[1][1] - data[2][1]) <= 1)
        while data[1][1] or data[2][1]:
            t = 1 if data[1][1] >= data[2][1] else 2
            s += data[t][0]
            data[t][1] -= 1
        s = s.replace('R', 'R' + 'GR' * G, 1)
        s = s.replace('B', 'B' + 'OB' * O, 1)
        s = s.replace('Y', 'Y' + 'VY' * V, 1)
    print("Case #%s: %s" % (case + 1, s, ))
