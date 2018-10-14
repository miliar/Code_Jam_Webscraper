#!/usr/bin/env python


ncase = int(raw_input())
for casenu in range(1, ncase + 1):
    n = int(raw_input())
    data = [int(i) for i in raw_input().split()]
    xorsum = 0
    for i in data:
        xorsum ^= i
    if xorsum:
        ans = "NO"
    else:
        ans = str(sum(data) - min(data))
    print "Case #%d: %s" % (casenu, ans)

