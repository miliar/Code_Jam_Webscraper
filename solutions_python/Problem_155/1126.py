#! /usr/bin/env python

t = int(input())

for ti in range(1, t+1):
    smax, audience = input().rstrip('\n').split(' ')
    audience = [int(x) for x in list(audience)]
    standing = 0
    invited = 0
    
    for k in range(len(audience)):
        m = k - standing

        if m > 0:
            invited += m
            standing += m

        standing += audience[k]

    print("Case #{}: {}".format(ti, invited))

