
from functools import reduce

T = int(input())
for i in range(0, T):
    data = list(map(int, input().split()))
    N = data[0]
    K = data[1]

    U = float(input())

    P = list(map(float, input().split()))
    P.sort()

    while U > 0 and P[0] < 1:
        lowest = P[0]
        highest = 1
        for j in range(K):
            if P[j] != lowest:
                highest = P[j]
                j -= 1
                break

        # Iterate 0->j-1
        add = min(U / (j+1), (highest - lowest))
        for k in range(j+1):
            P[k] += add
        U -= (j+1) * add

    prob = reduce(lambda x,y: x*y, P)
    print("Case #%d: %f" % ((i+1), prob))