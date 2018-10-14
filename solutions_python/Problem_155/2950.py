for n in xrange(1, input()+1):
    smax, shyness = raw_input().split()
    smax = int(smax)
    shyness = map(int, shyness)
    standing = 0
    ans = 0
    for i in xrange(smax+1):
        if shyness[i] > 0 and i > standing:
            ans += i-standing
            standing = i
        standing += shyness[i]
    print "Case #"+str(n)+": "+str(ans)
