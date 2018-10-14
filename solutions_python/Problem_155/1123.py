#!/usr/bin/python3

T = int(input())

for t in range(T):
    S_max, array = input().strip().split()
    n = 0
    answer = 0
    for i, c in enumerate(array):
        if int(c) > 0 and i > n:
            answer += i - n
            n += i - n
        n += int(c)
    print("Case #%d: %d" % (t+1, answer))
