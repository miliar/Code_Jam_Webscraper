T = int(raw_input())

def solve(t):
    (Smax, counts) = raw_input().split()
    added = 0
    total = 0
    for i in xrange(len(counts)):
        Si = int(counts[i])
        delta = i - total
        if delta > 0:
            added += delta
            total += delta
        total += Si

    print "Case #%s: %s" % (t, added)

for t in xrange(T):
    solve(t+1)
