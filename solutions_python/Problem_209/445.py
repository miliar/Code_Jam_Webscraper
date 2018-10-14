from math import pi
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    P = []
    for i in range(0, n):
        r, h = map(int, input().split())
        P.append((r, h, r*h*2, r**2))
    P = sorted(P, key =lambda x: -x[2])
    best = 0
    for i in range(0, n):
        base = P[i][3]
        side = P[i][2]
        cnt = 1
        for j in range(0, n):
            if cnt == k:
                best = max(best, base+side)
                break
            if i == j or P[j][3] > base:
                continue
            cnt+=1
            side+=P[j][2]
        
            
    area = 0
    print("Case #{0}: {1}".format(t, best*pi))