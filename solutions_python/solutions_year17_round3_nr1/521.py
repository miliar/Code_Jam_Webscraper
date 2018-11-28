from math import pi


def val_outer(R, H):
    return 2 * pi * R * H


t = int(input())
for i in range(1, t + 1):
    N, K = [int(s) for s in input().split(" ")]
    pancakes = []
    for j in range(N):
        R, H = [int(s) for s in input().split(" ")]
        pancakes.append((R, H, val_outer(R, H)))

    sorted_by_radius = sorted(pancakes, key=lambda x: x, reverse=True)

    max_res = 0

    for j in range(N - K + 1):
        max_radi = sorted_by_radius[j]
        res = val_outer(max_radi[0], max_radi[1])
        res += pi * max_radi[0] * max_radi[0]
        sor = sorted(sorted_by_radius[(j+1):], key=lambda x: x[2], reverse=True)
        # print('picked:', max_radi)
        # print('sorted:', sor)
        res += sum(map(lambda x: x[2], sorted(sorted_by_radius[(j+1):], key=lambda x: x[2], reverse=True)[:(K-1)]))
        if res > max_res:
            max_res = res

    print("Case #{}: {}".format(i, max_res))
