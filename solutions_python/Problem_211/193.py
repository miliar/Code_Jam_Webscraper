# -*- coding: utf-8 -*-

f = open('C-small.in', 'r')
out = open('answer.txt', 'w+')

from functools import reduce

def solve(p, unit, n, k):
    start = n - k
    i = start
    while (unit > 1e-8):
        #print(p)
        if i + 1 >= len(p):
            break
        diff = p[i + 1] - p[i]
        if (i - start + 1) * diff < unit:
            for j in range(start, i + 1):
                p[j] += diff
            unit -= (i - start + 1) * diff
        else:
            diff = unit / (i - start + 1)
            for j in range(start, i + 1):
                p[j] += diff
            break
        i += 1

t = int(f.readline())
for i in range(t):
    n, k = (int(ch) for ch in f.readline().split())
    unit = float(f.readline())
    p = [float(ch) for ch in f.readline().split()]
    p.sort()
    p.append(1)
    solve(p, unit, n, k)
    answer = reduce(lambda x, y: x * y, p)       
    out.write('Case #' + str(i + 1) + ': ' + "{:.8f}".format(answer)+'\n')

f.close()
out.close()