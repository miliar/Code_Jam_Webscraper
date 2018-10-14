for t in xrange(1, input() + 1):
    flip = 0
    s, k = raw_input().split()
    s = list(s)
    k = int(k)
    for i in xrange(len(s) - k + 1):
        if s[i] == '+':
            continue
        else:
            flip += 1
            for j in xrange(i, i + k):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
    if '-' in s[len(s) - k:]:
        print 'Case #%d: IMPOSSIBLE' % t
    else:
        print 'Case #%d: %d' % (t, flip)
