#!/usr/bin/python

import sys

f = sys.stdin

tt = eval(f.readline().strip())

def count(a):
    s = [0]
    for i in range(1, len(a)):
        tmp = 0
        for j in range(0, i):
            if a[j] > a[i]:
                tmp += 1
        s.append(tmp)
    return s

for cc in range(1, tt + 1):
    tmp = f.readline()
    tmp = tmp.split()
    n = eval(tmp[0])
    tmp = f.readline()
    a = tmp.split()
    for i in range(0, n):
        a[i] = eval(a[i])
    l = count(a)
    a.reverse()
    r = count(a)
    ans = 0
    for i in range(0, n):
        if l[i] < r[n - 1 - i]:
            tmp = l[i]
        else:
            tmp = r[n - 1 - i]
        ans += tmp
    print "Case #%d: %d" % (cc, ans)
