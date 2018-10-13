#! /usr/bin/env python
import math

cases = int(raw_input())
for case in range(0, cases):
    ip = raw_input().split(' ')    
    n = int(ip[0])
    k = int(ip[1])

    a = []
    a.append(n)
    for i in range(0, int(math.log(k, 2))):
        b = []
        for x in a:
            if x % 2 == 0:
                b.append(x/2 - 1)
                b.append(x/2)
            else:
                b.append((x-1)/2)
                b.append((x-1)/2)
        a = b
    a.sort(reverse=True)
    left = k - 2**(int(math.log(k, 2)))
    r = a[left]
    if r % 2 == 0:
        print("Case #{}: {} {}".format(case + 1, r/2, r/2 - 1))
    else:
        print("Case #{}: {} {}".format(case + 1, (r-1)/2, (r-1)/2))
