import sys

(_stdin, sys.stdin) = (sys.stdin, open('A-large-practice.in', 'r'))
(_stdout, sys.stdout) = (sys.stdout, open('A-large.out', 'w'))

T = int(input())


def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


for t in range(1, T+1):
    P, Q = map(int, input().split('/'))
    P, Q = P // gcd(P, Q), Q // gcd(P, Q)
    if Q & (Q-1):
        print('Case #%d: impossible' % t)
    else:
        ans = 0
        while P < Q:
            ans += 1
            Q >>= 1
        print('Case #%d: %d' % (t, ans))