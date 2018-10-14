"""https://code.google.com/codejam/contest/dashboard?c=3264486#s=p0"""

def solve(st, k):
    l = [0 if x == '+' else 1 for x in st]
    k = int(k)
    n = len(l)
    res = 0
    while True:
        try:
            left, right = l.index(1), n - 1 - l[::-1].index(1)
        except ValueError:
            return res
        if right < left + k - 1:
            return 'IMPOSSIBLE'
        for i in range(left, left + k):
            l[i] = l[i] ^ 1
        res += 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        res = solve(*input().split())
        print('Case #{}: {}'.format(i + 1, res))
