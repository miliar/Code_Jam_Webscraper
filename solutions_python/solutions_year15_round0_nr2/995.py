__author__ = 'Levan Kasradze'

import heapq


def f(p):
    a = heapq.heappop(p)
    res = -a
    if a < -1:
        for i in range(2, res // 2 + 1):
            q = p.copy()
            heapq.heappush(q, -i)
            heapq.heappush(q, a + i)
            res = min(res, f(q) + 1)
    return res


with open('b.in', 'r') as fin:
    with open('b.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            print(i)
            fout.write('Case #' + str(i) + ': ')
            d = fin.readline()
            p = [-int(j) for j in fin.readline().split()]
            heapq.heapify(p)
            fout.write(str(f(p)) + '\n')