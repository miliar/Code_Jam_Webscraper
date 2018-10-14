import math
from itertools import combinations


def solve():
    f = open("A-small-attempt0.in", "r")
    T = int(f.readline())
    out = open("output.out", "w")

    for case in range(T):
        N, K = map(int, f.readline().split())
        size = []
        for i in range(N):
            r, h = map(int, f.readline().split())
            size.append((r, h))
        size = sorted(size, reverse=True)
        max = -1
        for c in combinations(range(N), K):
            ans = 2 * math.pi * size[c[0]][0] * size[c[0]][1]
            for i in range(1, K):
                ans = ans + 2 * math.pi * size[c[i]][0] * size[c[i]][1]
                if size[c[i]][0] < size[c[i - 1]][0]:
                    ans = ans + (math.pi * (size[c[i - 1]][0] ** 2) - math.pi * (size[c[i]][0] ** 2))
            ans = ans + math.pi * (size[c[K - 1]][0] ** 2)
            if ans > max:
                max = ans
        print('Case #%d: %f' % (case + 1, max))
        out.write('Case #%d: %f\n' % (case + 1, max))

solve()