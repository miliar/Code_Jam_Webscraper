for case in xrange(1, int(raw_input()) + 1):
    print "Case #%d:" % case,

    n, k = map(int, raw_input().split())

    x = 2 ** n - 1
    if k < x:
        print "OFF"
    elif k == x:
        print "ON"
    elif k % (x + 1) == x:
        print "ON"
    else:
        print "OFF"
