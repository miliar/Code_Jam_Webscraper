#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    m, _, s = input().partition(' ')
    m = int(m)
    standing = 0
    friends = 0
    for i in range(m+1):
        if standing < i:
            friends += (i - standing)
            standing = i
        standing += int(s[i])
    print("Case #{}: {}".format(t, friends))

