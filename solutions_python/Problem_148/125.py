t = int(raw_input())
for kei in xrange(t):
    n, x = [int(y) for y in raw_input().split()]
    s = [int(y) for y in raw_input().split()]
    s = sorted(s)
    s.reverse()
    count = 0
    # print s
    for i in xrange(len(s)):
        if s[i] < 0:
            continue
        for j in xrange(i+1, len(s)):
            if s[j] < 0:
                continue
            if s[i] + s[j] <= x:
                s[i] = s[j] = -1
                count += 1
                break
        if s[i] > 0:
            s[i] = -1
            count += 1
        # print s
    print "Case #%d: %d" % (kei+1, count)
