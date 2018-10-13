# -*- coding: utf-8 -*-

T = int(raw_input())
for case in xrange(1, T + 1):
    x = map(int, raw_input().split())
    N = x[0]
    S = x[1:]
    S.sort()

    found = False
    d = {}
    for s in S:
        if s in d:
            print 'Case #%d:' % case
            print s
            print ' '.join(map(str, d[s]))
            found = True
            break

        for k, v in d.items():
            if k + s in d:
                print 'Case #%d:' % case
                s1 = set(d[k + s])
                s2 = set(v + [s])
                sc = s1 & s2
                s1 -= sc
                s2 -= sc
                print ' '.join(map(str, s1))
                print ' '.join(map(str, s2))
                found = True
                break
            else:
                d[k + s] = v + [s]
        d[s] = [s]
        if found:
            break
    if not found:
        print 'Case #%d: Impossible' % case

