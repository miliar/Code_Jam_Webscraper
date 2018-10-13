#! /usr/bin/python3

tc = int(input().strip())

for t in range(tc):

    from collections import deque

    a, k = [x for x in input().strip().split()]
    k = int(k)
    a += '+'

    d = deque()
    res = 0

    for i, x in enumerate(a):
        if len(d):
            if d[0] == i:
                d.popleft()
        if (x == '+') != (len(d)%2 == 0):
            d.append(i+k)
            res += 1

    print('Case #{}: {}'.format(t+1, 'IMPOSSIBLE' if len(d) else str(res)))
