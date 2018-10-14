#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    r1 = int(input())
    C1 = []
    for i in range(4):
        C1.append([int(x) for x in input().split()])
    r2 = int(input())
    C2 = []
    for i in range(4):
        C2.append([int(x) for x in input().split()])

    inter = set(C1[r1-1]).intersection(set(C2[r2-1]))

    message = ""
    if len(inter) == 0:
        message = "Volunteer cheated!"
    elif len(inter) == 1:
        message = str(list(inter)[0])
    else:
        message = "Bad magician!"
    print("Case #{}: {}".format(t, message))

