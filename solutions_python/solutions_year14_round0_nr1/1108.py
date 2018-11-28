# -*- coding: utf-8 -*-

t = int(raw_input())

for i in xrange(1, t+1):
    a = int(raw_input())
    b = []
    for j in xrange(4):
        b.append([int(e) for e in raw_input().split()])
    c = int(raw_input())
    d = []
    for j in xrange(4):
        d.append([int(e) for e in raw_input().split()])
    bb = set(b[a-1])
    dd = set(d[c-1])
    res = len(bb & dd)
    if res == 0:
        ans = 'Volunteer cheated!'
    elif res == 1:
        ans = list(bb & dd)[0]
    else:
        ans = 'Bad magician!'
    print 'Case #%d:' % i, ans
