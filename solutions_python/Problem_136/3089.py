#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    C, F, X = [float(x) for x in input().split()]

    bonus = 0.
    speed = 2.

    while X/speed > C/speed + X/(speed+F):
        bonus += C/speed
        speed += F

    print("Case #{}: {}".format(t, bonus + X/speed))
