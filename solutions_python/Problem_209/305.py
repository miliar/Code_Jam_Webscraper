from math import pi

def area(r, h):
    return 2 * pi * r * h

def area_t(r):
    return pi * r * r

T = int(input())

for i in range(1, T+1):
    print(f'Case #{i}: ', end='')

    N, K = map(int, input().split())
    P = []

    for j in range(N):
        r, h = map(int, input().split())
        P.append((area(r, h), r, h))

    P.sort(reverse=True)

    A = P[:K]
    B = P[K:]

    r_max = max(p[1] for p in P[:K])
    r = max(p[1] for p in P)

    if K == N or r_max == r:
        r_max = max(p[1] for p in P[:K])
        area_top = pi * r_max * r_max
        area_side = sum(p[0] for p in P[:K])

        print("%.9f" % (area_top + area_side))
    else:
        h = 0
        for p in P[K:]:
            if r == p[1] and h < p[2]:
                h = p[2]

        xx = (area(r, h) + area_t(r) - area_t(r_max))
        if xx > P[K-1][0]:
            P[K-1] = (area(r, h), r, h)

        r_max = max(p[1] for p in P[:K])
        area_top = pi * r_max * r_max
        area_side = sum(p[0] for p in P[:K])

        print("%.9f" % (area_top + area_side))
