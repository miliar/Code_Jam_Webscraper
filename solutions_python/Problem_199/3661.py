import sys

sys.setrecursionlimit(10000)


def flip(p):
    return '+' if p == '-' else '-'


def solve(s, k):
    sp = s.count('+')
    sl = len(s)
    if sp == sl:
        return 0
    if k == sl:
        if sp == 0:
            return 1
        else:
            return 'IMPOSSIBLE'
    if s[0] == '+':
        if (sl - 1) >= k:
            return solve(s[1:], k)
        else:
            return 'IMPOSSIBLE'
    else:
        for i, p in enumerate(s[:k]):
            s[i] = flip(p)
        ns = solve(s[1:], k)
        if ns == 'IMPOSSIBLE':
            return ns
        else:
            return 1+ns


if __name__ == '__main__':
    t = int(input())
    for n in range(1, t+1):
        s, k = input().split(' ')
        s = list(s)
        k = int(k)
        print('Case #{}: {}'.format(n, solve(s, k)))
