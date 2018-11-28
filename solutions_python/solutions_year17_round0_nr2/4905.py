for t in xrange(int(raw_input())):
    N = int(raw_input())
    if N > 9:
        for i in xrange(N, 9, -1):
            for j in xrange(len(str(i))-1, 0, -1):
                flag = True
                if int(str(i)[j-1]) > int(str(i)[j]):
                    flag = False
                    break
            if flag is True:
                ans = i
                break
        if flag is False:
            ans = 9
    else:
        ans = N

    print "Case #%d: %s" % (t+1, ans)
