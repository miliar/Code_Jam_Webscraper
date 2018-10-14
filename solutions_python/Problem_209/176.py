import functools
import math

def cmp_x(a, b):
    ra, ha = a
    rb, hb = b
    pa = ra * ha
    pb = rb * hb
    if pa > pb:
        return -1
    elif pa == pb:
            return 0
    else:
        return 1


T = int(input())
for tid in range(T):
    A = []
    N, K = [int(x) for x in input().split(' ')]
    for i in range(N):
        r, h = [int(x) for x in input().split(' ')]
        A.append((r, h))
    A.sort(key = functools.cmp_to_key(cmp_x))
    maximum = 0
    for i in range(len(A)):
        ra, ha = A[i]
        plocha = ra * ra + 2 * ra * ha
        count = 1
        for j in range(len(A)):
            if count >= K:
                break
            if i != j:
                rx, hx = A[j]
                count+=1
                plocha += 2 * rx * hx
        maximum = max(maximum, plocha)
    result = maximum * math.pi
    print('Case #{}: {}'.format(tid + 1, str(result)))
