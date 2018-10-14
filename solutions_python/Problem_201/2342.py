import math
from heapq import heappush, heappop


def solve():
    f = open("C-small-2-attempt0.in", "r")
    T = int(f.readline())
    out = open("output.out", "w")

    for case in range(T):
        N, K = map(int, f.readline().split())
        heap = []
        heappush(heap, -N)
        lenght = 0
        for x in range(K):
            lenght = - heappop(heap)
            if lenght > 1:
                l = lenght - 1
                if l == 1:
                    heappush(heap, - (lenght - 1))
                else:
                    heappush(heap, -(l // 2))
                    heappush(heap, -(l // 2 + (1 if l % 2 == 1 else 0)))

        y = (lenght - 1) // 2 + (1 if (lenght - 1) % 2 == 1 else 0)
        z = (lenght - 1) // 2

        print('Case #%d: %d %d' % (case + 1, y, z))
        out.write('Case #%d: %d %d\n' % (case + 1, y, z))


solve()
