t = input()
i = 0
while t:
    i += 1
    t -= 1
    d, n = raw_input().split()
    d = int(d)
    n = int(n)
    maxTime = 0
    while n:
        n -= 1
        k, s = raw_input().split()
        k = int(k)
        s = int(s)
        timeTaken = (d - k) / float(s)
        if timeTaken > maxTime:
            maxTime = timeTaken

    if maxTime == 0:
        print "Something wrong happened"

    print "Case #" + str(i) + ": " + str('{0:.6f}'.format(d / float(maxTime)))
