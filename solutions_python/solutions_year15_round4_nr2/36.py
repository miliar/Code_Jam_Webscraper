from re import *
from sys import stderr
def readint():
    return int(input())
def readfloat():
    return float(input())
def readarray(N, foo=input):
    return [foo() for i in range(N)]
def readlinearray(foo=int):
    return list(map(foo, input().split()))

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


def cmp_eq(a, b):
    return abs(a - b) < 1e-10

case_number = readint()
for case in range(case_number):
    N, V, X = input().split()
    N = int(N)
    V = float(V)
    X = float(X)
    a = [readlinearray(float) for i in range(N)]
    if N == 1:
        if cmp_eq(a[0][1], X):
            answer = V / a[0][0]
        else:
            answer = "IMPOSSIBLE"
    else:
        a.sort(key=lambda x:x[1])
        if cmp_eq(a[0][1], X) or cmp_eq(a[1][1], X) or a[0][1] <= X <= a[1][1]:
            if cmp_eq(a[0][1], a[1][1]):
                answer = V / (a[0][0] + a[1][0])
            else:
                y2 = (X * V - V * a[0][1]) / (a[1][1] - a[0][1])
                y1 = V - y2
                x1 = y1 / a[0][0]
                x2 = y2 / a[1][0]
                answer = max(x1, x2)
        else:
            answer = "IMPOSSIBLE"
    if isinstance(answer, float):
        answer = "%.10f" % (answer, )
    print("Case #%s: %s" % (case + 1, answer))
