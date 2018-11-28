#!/usr/bin/env python3

# Google Code Jam Round 2 2017
# Problem A. Fresh Chocolate
# Solution in Python 3
# By Smithers

for x in range(1, int(input()) + 1):
    n, p = map(int, input().split())
    g = list(map(int, input().split()))
    
    h = [0] * p
    for i in g:
        h[i % p] += 1
    
    if p == 2:
        y = h[0] + (h[1] + 1) // 2
    elif p == 3:
        y = h[0] + min(h[1], h[2]) + (abs(h[1] - h[2]) + 2) // 3
    elif p == 4:
        y = h[0] + h[2] // 2 + min(h[1], h[3])
        a = h[2] % 2
        b = abs(h[1] - h[3])
        if a == 1:
            if b >= 2:
                y += 1 + (b - 2 + 3) // 4
            else:
                y += 1
        else:
            y += (b + 3) // 4
    else:
        raise RuntimeError
    
    print('Case #{}: {}'.format(x, y))
