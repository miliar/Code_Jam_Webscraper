import math

def solve():
    N, K = (int(x) for x in input().split())
    P = [tuple(int(x) for x in input().split()) for _ in range(N)]
    P.sort(key=lambda rh: 2*rh[0]*rh[1], reverse=True)

    #print (P)
    res = 0
    for i in range(N):
        r, h = P[i]
        cur = r*r + 2*r*h
        left = K - 1
        #L = [P[i]]
        for k in range(N):
            if left <= 0: break
            if i == k: continue
            rk, hk = P[k]
            if rk > r: continue
            cur += 2*rk*hk
            left -= 1
            #L.append(P[k])

        #print (L, cur)
        res = max(res, cur)

    return math.pi * float(res)

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %.6f" % (t, solve()))
