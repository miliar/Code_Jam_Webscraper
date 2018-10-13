#!/usr/bin/python2

def method1(N, m):
    eaten = 0
    for i in range(N - 1):
        eaten += max(m[i] - m[i + 1], 0)
    return eaten

def method2(N, m):
    # find the max mushrooms provably eaten
    rate = 0
    for i in range(N - 1):
        rate = max(rate, max(m[i] - m[i + 1], 0))

    eaten = 0
    for i in range(N - 1):
        eaten += min(rate, m[i])

    return eaten

T = int(raw_input().split()[0])

for case in range(T):
    N = int(raw_input().split()[0])
    m = map(int, raw_input().split())

    y = method1(N, m)
    z = method2(N, m)

    print 'Case #' + str(case + 1) + ': ' + str(y) + ' ' + str(z)
