import sys
from math import pi
from operator import itemgetter

def solve():
    T = int(sys.stdin.readline())

    for tc in range(T):
        N, K = map(int, sys.stdin.readline().split())
        panc = []

        for i in range(N):
            ri, hi = map(int, sys.stdin.readline().split())
            panc.append((ri, hi, 2 * pi * ri * hi))

        ans = 0

        panc.sort(key=itemgetter(0), reverse=True)

        for i in range(N - K + 1):
            area = panc[i][0]**2 * pi + panc[i][2]

            panc_s = sorted(panc[i + 1:], key=itemgetter(2), reverse=True)

            for pan in panc_s[:K - 1]:
                area += pan[2]

            ans = max(area, ans)

        print('Case #{}: {}'.format(tc + 1, ans))


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

if __name__ == '__main__':
    solve()