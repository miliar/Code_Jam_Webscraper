import sys

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    Smax, S = raw_input().split()
    # Smax = int(Smax)
    S = map(int, S)


    clapping = 0
    invited = 0
    for sl, count in enumerate(S):
        if count == 0:
            continue
        if sl > clapping:
            invited += sl - clapping
            clapping += sl - clapping
        clapping += count
    print invited

