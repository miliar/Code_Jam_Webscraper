import math

def fill_stalls(N, K):
    gaps = {0 : N}
    for _ in range(K):
        maxGapIndex = max(gaps, key=gaps.get)
        maxGapValue = gaps[maxGapIndex]
        R = math.floor(maxGapValue / 2)
        L = maxGapValue - R - 1
        gaps[maxGapIndex] = L
        gaps[maxGapIndex + L + 1] = R
    gaps = {k:v for k, v in gaps.items() if v != 0}
    return L, R

def new_fill_stalls(N, K):
    gaps = {N : 1}
    for _ in range(K):
        maxGap = max(gaps)
        R = math.floor(maxGap / 2)
        L = maxGap - R - 1
        gaps[maxGap] -= 1
        gaps[L] = gaps.get(L, 0) + 1
        gaps[R] = gaps.get(R, 0) + 1
        gaps = {k:v for k, v in gaps.items() if v != 0}
    return L, R

t = int(input())
for n in range(t):
    inputs = input().split()
    L, R = new_fill_stalls(int(inputs[0]), int(inputs[1]))
    print("Case #{}: {} {}".format(n+1, max(L,R), min(L,R)))
