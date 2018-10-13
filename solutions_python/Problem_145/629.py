#!/usr/bin/python
# vi: set fileencoding=utf-8 :

def GCD(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def is_power2(x):
    power = 0
    while x > 1:
        q = x / 2
        r = x % 2
        if r == 1:
            return 'impossible'
        power += 1
        x = q
    return power

def solve(P, Q):
    gcd = GCD(Q, P)
    P, Q = P / gcd, Q / gcd
    power = is_power2(Q / gcd)
    if power == 'impossible':
        return 'impossible'
    nearest_ancestor = 0
    while P < Q:
        Q /= 2
        nearest_ancestor += 1
    return nearest_ancestor


T = int(raw_input())
for t in range(T):
    line = raw_input()
    P, Q = map(int, line.split('/'))
    print 'Case #' + str(t + 1) + ':', solve(P, Q)
