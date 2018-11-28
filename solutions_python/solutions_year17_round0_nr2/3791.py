t = int(raw_input())
for c in xrange(1, t + 1):
    n = raw_input()
    if len(n) == 1:
        print 'Case #%s: %s' % (c, n)
    else:
        if int(n) % 10 == 0:
            n = str(int(n)-1)
        l = len(n)
        i = l - 1
        tidy = False
        while not tidy:
            while i > 0:
                if int(n[i]) - int(n[i - 1]) >= 0:
                    tidy = True
                    i -= 1
                else:
                    tidy = False
                    n = n[0:i-1] + str(int(n[i - 1]) - 1) + '9' * (l - i)
        print 'Case #%s: %d' % (c, int(n))
