t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()

    cur = 0
    highidx = 0
    problem = -1
    for idx, d in enumerate(s):
        if int(d) > cur:
            cur = int(d)
            highidx = idx
        elif int(d) == cur:
            pass
        else:
            problem = highidx
            break

    if problem == -1:
        print "Case #{}: {}".format(i, s)
    else:
        if highidx == 0:
            print "Case #{}: {}".format(i, (len(s) - 1) * '9')
        else:
            d = int(s[highidx])
            first = s[:highidx]
            middle = str(d-1)
            last = len(s[highidx+1:]) * '9'
            print "Case #{}: {}".format(i, first + middle + last)
