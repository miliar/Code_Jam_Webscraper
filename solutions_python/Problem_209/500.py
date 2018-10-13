#Henry Maltby
#Code Jam 2017

import math

def ample_syrup(dims, k):
    """
    .
    """
    N = len(dims)
    dims.sort(key=lambda x: - x[0])
    area_sorted = list(dims)
    area_sorted.sort(key=lambda x: - x[0] * x[1])
    ans = 0
    for i in range(N):
        if N - i < k:
            break
        R = dims[i][0]
        test, count = R * R + 2 * R * dims[i][1], 1
        lst = list(area_sorted)
        lst.pop(lst.index(dims[i]))
        for j in range(N):
            if count == k:
                break
            if R >= lst[j][0]:
                test += 2 * lst[j][0] * lst[j][1]
                count += 1
        ans = max(ans, math.pi * test)
    return ans

def A():
    """
    Runs the problem as dictated in problem spec.
    """
    f = open('A-large.in')
    g = open('A-large.out', 'w')

    T = int(f.readline())
    for i in range(T):
        N, K = [int(x) for x in f.readline().strip().split(' ')]
        dimensions = []
        for j in range(N):
            R, H = [int(x) for x in f.readline().strip().split(' ')]
            dimensions.append((R, H))
        ans = ample_syrup(dimensions, K)
        g.write("Case #" + str(i + 1) + ": " + "{0:.6f}".format(ans))
        if i != T - 1:
            g.write("\n")

A()
