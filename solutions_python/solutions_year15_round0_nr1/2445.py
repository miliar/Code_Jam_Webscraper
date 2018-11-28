#!/usr/bin/env python3

t = int(input().strip())

for i in range(t):
    smax, shy_str = input().strip().split(' ', 1)
    smax = int(smax)
    shyness = []
    for n in shy_str:
        shyness.append(int(n))
    others = 0
    for j in range(len(shyness)):
        if j != 0 and sum(shyness[:j]) + others < j:
            others += j - (sum(shyness[:j]) + others)

    print("Case #{}: {}".format(i + 1, others))

