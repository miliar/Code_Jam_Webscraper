def main():
    # read in number of samples
    N = int(raw_input().strip())

    for i in xrange(N):
        engines = {}
        S = int(raw_input().strip())
        for j in xrange(S):
            engines[raw_input().strip()] = 0
        Q = int(raw_input().strip())
        other_engines = {}
        changes = 0
        for j in xrange(Q):
            q = raw_input().strip()
            present = engines.get(q, None)
            if present is None:
                continue
            if len(engines) == 1:
                changes += 1
                t = other_engines
                other_engines = engines
                engines = t
            else:
                del engines[q]
                other_engines[q] = 1
        print "Case #%d: %d" % (i + 1, changes)

main()
