def solve(Smax, aud):
    standing = aud[0]
    maxneed = 0
    for si in xrange(1, Smax+1):
        need = si - standing
        maxneed = max(need, maxneed)
        standing += aud[si]
    return maxneed

s = raw_input()
T = int(s)
for t in xrange(0, T):
    s = raw_input()
    Smax, digits = s.split()
    Smax = int(Smax)
    aud = map(lambda dig: ord(dig)-ord('0'), digits)
    #print Smax, digits, aud
    print "Case #{0}: {1}".format(t+1, solve(Smax, aud))
    