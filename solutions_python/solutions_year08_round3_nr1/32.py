#!/usr/bin/python2.5

for case in range(input()):
    P, K, L = [int(x) for x in raw_input().split()]
    f = [int(x) for x in raw_input().split()]
    f.sort()
    k = {}
    for i, l in enumerate(reversed(f)):
        k.setdefault(i % K, []).append(l)
    n = 0
    for lst in k.itervalues():
        n += sum([(i + 1) * v for i, v in enumerate(lst)])

    print "Case #%s: %s" % (case + 1, n)

