for x in xrange ( input() ):
    n = input()
    left = {}
    right = {}
    sects = 0
    for i in xrange(n):
        # get heights
        h1,h2 = (int(j) for j in raw_input().split())
        left[h1] = 1
        right[h2] = 1

        # left above, right below
        LA = len ( [f for f in left.keys() if f > h1] )
        RB = len ( [f for f in right.keys() if f < h2] )
        shit1 = min(LA,RB)

        # left below, right above
        LB = len ( [f for f in left.keys() if f<h1] )
        RA = len ( [f for f in right.keys() if f>h2] )
        shit2 = min(LB,RA)

        l = [ k for k in [shit1,shit2] if k > 0]
        if (len(l)>0):
            sects+=min(l)

    print "Case #%d:" % (x+1), sects

