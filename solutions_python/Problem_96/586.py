#!/usr/bin/env python2

f = open('i', 'r')

n = int(f.readline()[:-1])

for i in range(n):
    s = f.readline()[:-1]
    ary = s.split(' ')
    N = int(ary[0])
    S = int(ary[1])
    p = int(ary[2])
    g = map(lambda x:int(x), ary[3:])
    ans = 0
    to = 0
    for j in g:
        x = j / 3
        mx = j - x * 2
        if mx - x == 2:
            if x + 1 >= p:
                ans += 1
            elif mx >= p:
                to += 1
        elif mx - x == 1:
            if mx >= p:
                ans += 1
        else:
            if x >= p:
                ans += 1
            elif x > 0 and x + 1 >= p:
                to += 1
    ans += min(to, S)
    print 'Case #%d: %d' % (i+1, ans)
