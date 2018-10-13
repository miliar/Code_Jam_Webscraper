import sys

t = int(sys.stdin.readline())
for i in xrange(t):
    s = sys.stdin.readline().split(' ');
    n = int(s[0])
    k = int(s[1])
    k %= 1 << n
    print 'Case #%d:' % (i + 1),
    if k == (1 << n) - 1:
        print 'ON'
    else:
        print 'OFF'