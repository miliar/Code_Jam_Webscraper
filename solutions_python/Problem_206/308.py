T = int(raw_input())

for t in xrange(T):

    D, N = map(int, raw_input().split())
    minn = None
    for n in xrange(N):
        start, speed = map(int, raw_input().split())
        hour = (D - start) / float(speed)
        x = D / float(hour)

        if minn == None or x < minn:
            minn = x

    print "Case #" + str(t+1) + ": " + str(minn)