cases = raw_input()
for case in xrange(int(cases)):
    q = map(int, raw_input().split())
    N, S, p = q[:3]
    t = q[3:]

    ans = 0
    for i in t:
        if i / 3 >= p:
            ans += 1
        elif i % 3 == 0:
            if i == 0:
                if p == 0:
                    ans += 1
            elif S > 0 and (i / 3) + 1 >= p:
                ans += 1
                S -= 1
        elif i % 3 == 1 and (i / 3) + 1 >= p:
            ans += 1
        else:
            if (i / 3) + 1 >= p:
                ans += 1
            elif S > 0 and (i / 3) + 2 >= p:
                ans += 1
                S -= 1
    print 'Case #%d: %s' % (case + 1, ans)
