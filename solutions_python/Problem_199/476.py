for _ in xrange(input()):
    print "Case #%d:" % (_+1),
    s, k = raw_input().split()
    s = [c is '+' for c in s]
    k = int(k)
    l = len(s)
    ans = 0
    for i in xrange(l-k+1):
        if s[i] == 0:
            for j in xrange(k):
                s[i+j] ^= 1
            ans += 1
    print ans if sum(s)==l else "IMPOSSIBLE"
