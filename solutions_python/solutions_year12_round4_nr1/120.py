#!/usr/bin/env python3
import heapq

T = int(input())

for case in range(1, T+1):
    N = int(input())
    vines = [tuple(map(int, input().split()+[i])) for i in range(N)]
    D = int(input())
    vines = [(v[0]+min(v[1], v[0]), v[0], v[1], v[2]) for v in vines]
    #vines.sort(reverse=True)
    vines= vines[::-1]

    ansi = 0
    while vines[ansi][3] != 0:
        ansi += 1
    #print(vines, ansi)

    usable = [True for v in vines]
    max_swing = [v[0]-v[1] for v in vines]
    needed_swing = [D-v[1] for v in vines]

    future = []
    uv = []

    for i in range(N):
        v = vines[i]

        #while future and future[0][1] <= v[0] and future[0][2] <= v[1]:
        #    f = heapq.heappop(future)
        #    heapq.heappush(uv, (f[2], f[1]))

        #print(i, v, uv, future)
        #while uv and uv[0][1] > v[0]:
        #    heapq.heappop(uv)

        #print(i, v, uv, future)

        canreach = False
        minneeded = max_swing[i]
        if uv:
            t = uv[0]
            for t in uv:
                if t[1]-v[1] >= t[0] and v[1] >= t[0] and v[0] >= t[1]:
                    canreach = True
                    minneeded = min(minneeded, t[1]-v[1])
        if v[0] >= D:
            canreach = True
            minneeded = min(minneeded, D-v[1])

        usable[i] = canreach

        if usable[i]:
            v = vines[i]
            heapq.heappush(future, (v[1]-minneeded, v[1], minneeded))
            uv.append((minneeded, v[1]))

    ans = "YES" if usable[ansi] else "NO"

    print("Case #{}: {}".format(case, ans))


