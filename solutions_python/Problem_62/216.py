T = input()
for case in xrange(1,T+1):
    n, = map(int,raw_input().split())
    abs = sorted([map(int,raw_input().split()) for _ in xrange(n)])
    c = 0
    for i in xrange(n):
        for j in xrange(i):
            if abs[j][1] > abs[i][1]:
                c += 1
        # for j in xrange(i+1,n):
        #     if abs[j][1] < abs[i][1]:
        #         c += 1
    print "Case #%s: %s" % (case, c)
