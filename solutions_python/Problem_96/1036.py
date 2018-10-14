t = int(raw_input())

for tt in xrange(t):
    inp = [int(x) for x in raw_input().split(' ')]
    n = inp[0]
    s = inp[1]
    p = inp[2]
    tot = inp[3:]
    ans = 0
    for i in tot:
        mn = i / 3
        if (mn >= p) or (((mn + 1) == p) and (i % 3)):
            ans += 1
        else:
            if s:
                if ((mn + 2) == p) and ((i % 3) == 2):
                    ans += 1
                    s -= 1
                elif ((mn + 1) == p) and ((mn - 1) >= 0):
                    ans += 1
                    s -= 1
    print 'Case #%s: %s' % (tt + 1, ans)

