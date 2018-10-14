import sys
from itertools import combinations

rl = lambda: sys.stdin.readline().strip()

T = int(rl())


def check(n):
    inc = True
    for i in range(1, len(n)):
        if inc and n[i - 1] > n[i]:
            inc = False
        if not inc and n[i - 1] < n[i]:
            return False
    return True


def check_inc(n, f, t):
    for i in range(f + 1, t):
        if n[i - 1] > n[i]:
            return False
    return True


def check_dec(n, f, t):
    for i in range(f + 1, t):
        if n[i - 1] < n[i]:
            return False
    return True


def brute_force(n):
    from collections import deque
    Q = deque([(n, 0)])
    while Q:
        s, c = Q[0]
        if check(s):
            return c
        Q.popleft()
        for i in range(1, len(n)):
            ss = s[::]
            ss[i], ss[i - 1] = ss[i - 1], ss[i]
            Q.append((ss, c + 1))

for tcase in range(T):
    N = int(rl())
    n = map(int, rl().split())
    nn = n[::]
    ans = 987654321
    print >> sys.stderr, n
    for k in range(1, N + 1):
        for n in combinations(nn, k):
            nnn = nn[::]
            inc_part = list(n)
            dec_part = [_n for _n in nn if _n not in inc_part]

            ans1 = 0
            if inc_part:
                ii = sorted(inc_part)
                for idx, i in enumerate(ii):
                    where = nnn.index(i)
                    while idx < where:
                        nnn[where - 1], nnn[where] = nnn[where], nnn[where - 1]
                        where -= 1
                        ans1 += 1
            ans2 = 0
            if dec_part:
                dd = sorted(dec_part, reverse=True)
                for idx, d in enumerate(dd):
                    idx += len(inc_part)
                    where = nnn.index(d)
                    while idx < where:
                        nnn[where - 1], nnn[where] = nnn[where], nnn[where - 1]
                        where -= 1
                        ans2 += 1
            assert check(nnn)
            ans = min(ans, ans1 + ans2)
    print 'Case #%d: %d' % (tcase + 1, ans)
