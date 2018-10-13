#!/usr/bin/python

import sys

f = sys.stdin

tt = eval(f.readline().strip())

for cc in range(1, tt + 1):
    tmp = f.readline()
    tmp = tmp.split()
    n = eval(tmp[0])
    x = eval(tmp[1])
    tmp = f.readline()
    a = tmp.split()
    for i in range(0, n):
        a[i] = eval(a[i])
    a = sorted(a)
    ans = 0
    i = 0
    j = n - 1
    while i <= j:
        if a[i] + a[j] <= x:
            i += 1
            j -= 1
        else:
            j -= 1
        ans += 1
    print "Case #%d: %d" % (cc, ans)
