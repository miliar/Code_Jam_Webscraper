t = int(raw_input().strip())

for i in xrange(t):
    n = int(raw_input().strip())
    tidy = 0
    for nn in xrange(n, 0, -1):
        s = str(nn)
        if s == ''.join(sorted(s)):
            tidy = nn
            break
    print "Case #" + str(i+1) + ": " + str(tidy)
