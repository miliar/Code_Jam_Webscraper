T = int(raw_input().strip())

def isTidy(s):
    reference = 0
    ret = True
    for index, c in enumerate(s):
        _c = int(c)
        if _c >= reference:
            reference = _c
        else:
            ret = index
            break
    return ret

def fixTidy(s, l, stopAt):
    return str(int(s[0:stopAt]) - 1) + '9' * (l - stopAt)

for t in xrange(T):
    N = int(raw_input().strip())
    s = str(N)
    L = len(s)

    while True:
        stopAt = isTidy(s)
        if stopAt is True:
            print 'Case #%d: %d' % (t + 1, int(s))
            break
        else:
            s = fixTidy(s, L, stopAt)