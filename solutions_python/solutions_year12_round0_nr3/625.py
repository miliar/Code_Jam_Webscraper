#!/usr/bin/env python

t = int(input())
for case in range(1,t+1):
    a,b = map(int,input().strip().split())
    total = 0
    for i in range(a,b):
        s = str(i)
        prev = {i}
        for _ in range(len(s)-1):
            s = s[1:] + s[0]
            j = int(s)
            if s[0] == '0' or j in prev:
                continue
            prev.add(j)
            if i < j <= b:
                total += 1
    print('Case #{}: {}'.format(case, total))
