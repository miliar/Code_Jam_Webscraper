import itertools
import math


def valid1(a, b):
    c1 = a * (b // a)
    c2 = a * (b // a + 1)
    return c1 >= b / 1.1 or c2 <= b / 0.9


def valid2(a1, a2, b1, b2):
    c1 = min(math.ceil(b1 / 1.1 / a1), math.floor(b1 / 0.9 / a1))
    c2 = max(math.ceil(b1 / 1.1 / a1), math.floor(b1 / 0.9 / a1))
    d1 = min(math.ceil(b2 / 1.1 / a2), math.floor(b2 / 0.9 / a2))
    d2 = max(math.ceil(b2 / 1.1 / a2), math.floor(b2 / 0.9 / a2))
    for i in range(max(c1, d1), min(c2, d2) + 1):
        if (b1 / 0.9 >= a1 * i >= b1 / 1.1) and (b2 / 0.9 >= a2 * i >= b2 / 1.1):
            return True
    else:
        return False


T = int(input())

for t in range(1, T + 1):
    N, P = [int(_) for _ in input().split()]
    R = [int(_) for _ in input().split()]
    Q1, Q2 = [], []
    if N == 1:
        Q1 = [int(_) for _ in input().split()]
        ans = 0
        for q in Q1:
            if valid1(R[0], q):
                ans += 1
        print('Case #%d: %d' % (t, ans))
    else:
        Q1 = [int(_) for _ in input().split()]
        Q2 = [int(_) for _ in input().split()]
        ans = 0
        for q2 in itertools.permutations(Q2):
            ans_ = 0
            for i in range(P):
                if valid2(R[0], R[1], Q1[i], q2[i]):
                    ans_ += 1
            ans = max(ans, ans_)
        print('Case #%d: %d' % (t, ans))
