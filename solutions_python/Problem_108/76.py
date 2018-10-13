#!/usr/bin/env python
t = int(input())
for case in range(1,t+1):
    n = int(input())
    vines = [tuple(map(int,input().strip().split())) for _ in range(n)]
    d = int(input())
    m = [0 for _ in range(n)]
    m[0] = 2*min(vines[0][0], vines[0][1])
    possible = m[0] >= d
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if m[j] >= vines[i][0]:
                m[i] = max(m[i], vines[i][0]+min(vines[i][0]-vines[j][0],vines[i][1]))
        if m[i] >= d:
            possible = True
            break
    print('Case #{}: {}'.format(case, 'YES' if possible else 'NO'))
