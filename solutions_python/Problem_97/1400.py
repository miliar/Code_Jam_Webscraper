import sys

_ = sys.stdin.readline()
for case, line in enumerate(sys.stdin.readlines()):
    case += 1
    a, b = map(int, line.split())
    if a/10 == 0 and b/10 == 0:
        print 'Case #%d: 0' % case
    else:
        r = {}
        for i in xrange(a, b+1):
            n = m = str(i)
            for _ in n:
                m = m[-1] + m[:-1]
                if a <= i < int(m) <= b:
                    r[n+m] = 1
        print 'Case #%d: %d' % (case, len(r))
