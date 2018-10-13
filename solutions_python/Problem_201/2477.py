import math
t = int(input())

for i in range(1, t + 1):
    n, p = [int(s) for s in input().split(" ")]
    stalls = [n]

    for j in range(p):
        maximum = max(stalls)
        if maximum % 2 == 0:
            r = int(maximum/2)
            l = r - 1
        else:
            l = r = int((maximum-1)/2)
        stalls.insert(stalls.index(maximum)+1, r)
        stalls.insert(stalls.index(maximum), l)
        stalls[stalls.index(maximum)] = 0

    print("Case #{}: {} {}".format(i, max(l,r), min(l,r)))
