T = int(raw_input())
for t in xrange(T):
    N, L, H = [int(x) for x in raw_input().split(' ')]
    players = [int(x) for x in raw_input().split(' ')]
    answer = 'NO'
    for f in xrange(L, H+1):
        h = True
        for p in players:
            if p % f != 0 and f % p != 0:
                h = False
                break
        if h:
            answer = str(f)
            break
    print "Case #%d: %s" % (t + 1, answer)

