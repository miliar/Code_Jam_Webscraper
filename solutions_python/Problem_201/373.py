#!/usr/bin/env python

import queue

def f(n):
    return tuple(-i for i in ((n+1)//2 - 1, n+1 - (n+1)//2 - 1))

t = int(input())
for i in range(1, t+1):
    n, k = [int(s) for s in input().split(' ')]
    q = queue.PriorityQueue()
    q.put(f(n))

    d = {f(n): 1}
    c = 0
    while c < k:
        minimum, maximum = [-i for i in q.get()]
        if maximum == minimum == 0:
            break
        m = d[(-minimum, -maximum)]
        if f(maximum) not in d:
            q.put(f(maximum))
            d[f(maximum)] = m
        else:
            d[f(maximum)] += m
        if minimum:
            if f(minimum) not in d:
                q.put(f(minimum))
                d[f(minimum)] = m
            else:
                d[f(minimum)] += m
        c += m

    print(f'Case #{i}: {maximum} {minimum}')
