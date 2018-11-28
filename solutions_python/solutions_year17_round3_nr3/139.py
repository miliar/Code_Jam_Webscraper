#!/usr/bin/python3

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    if (N != K): raise Exception
    U = float(input())
    P = list(map(float, input().split()))

    P.sort()
    
    numEqual = 1
    prob = P[0]

    while numEqual < N:
        toDistribute = (P[numEqual] - prob) * numEqual
        if (toDistribute < U):
            U -= toDistribute
            prob = P[numEqual]
            numEqual += 1
        else:
            prob += U / numEqual
            U = 0
            break

    prob += U / N

    prob = min(prob, 1)

    ans = prob ** numEqual
    for i in range(numEqual, N):
        ans *= P[i]

    print("Case #{0}: {1}".format(case, ans))

