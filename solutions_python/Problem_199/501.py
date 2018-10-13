for t in xrange(input()):
    s, k = raw_input().split()
    s, k = list(s), int(k)
    a, q = 0, []
    print "Case #" + str(t+1) + ":",
    for i in xrange(len(s)-k+1):
        if (len(q) % 2) != (s[i] == '-'):
            q += [i]
            a += 1
        if len(q) > 0 and q[0] < i-k+2:
            del q[0]
    for i in xrange(len(s)-k+1, len(s)):
        if (len(q) % 2) != (s[i] == '-'):
            print "IMPOSSIBLE"
            break
        if len(q) > 0 and q[0] < i-k+2:
            del q[0]
    else:
        print a