#!/bin/python3


T = int(input().strip())
for test in range(T):
    N, K = [int(x) for x in input().split()]
    U = float(input().strip())
    probs = [(float(x),1) for x in input().split()]
    probs = sorted(probs, key=lambda x: x[0])
    while U > 0.0000001:
        # print(U)
        if len(probs) > 1:
            p1 = probs[0]
            p2 = probs[1]
            # print(p1,p2,len(probs))
            if ((p2[0] - p1[0]) * p1[1]) <= U:
                U -= ((p2[0] - p1[0]) * p1[1])
                probs[0] = (p2[0],p1[1]+1)
                probs = probs[:1] + probs[2:]
            else:
                probs[0]=(p1[0]+(U/p1[1]),p1[1])
                U = 0
        else:
            p1 = probs[0]
            probs[0]=(p1[0]+(U/p1[1]),p1[1])
            U = 0
    ans = 1
    for i in probs:
        ans *= i[0]**i[1]
    print('Case #%d: %f' % ((test + 1), ans))
