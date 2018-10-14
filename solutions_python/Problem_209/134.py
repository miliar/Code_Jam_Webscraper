# Google codejam 2017B
# A. 

import math

for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    l = []
    for _ in range(N):
        R, H = map(int, input().split())
        l.append((R*H, R, H))
    l.sort(key=lambda t: t[1], reverse=True)

    maxResult = 0
    #print("length=", len(l))
    for i in range(N - K + 1):
        result = math.pi * (l[i][1] ** 2 + 2 * l[i][0])
        #print(result, l[i][1])
        ll = sorted(l[i + 1:], key=lambda t: t[0], reverse=True)
        #print(ll)
        for k in range(K - 1):
            r, h = ll[k][1], ll[k][2]
            result += 2 * math.pi * r * h
            #print(result, r, h)
        #print(result)

        maxResult = max(maxResult, result)

    print ("Case #{}: {}".format(t, maxResult))
