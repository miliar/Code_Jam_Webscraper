import re
t = int(raw_input())
for i in xrange(1, t + 1):
    s = long(raw_input())
    for counter in xrange(s, 0, -1):
        res = [long(x) for x in str(counter)]
        if sorted(res) == res:
            ans = counter
            break
    print 'Case #%d: %s' % (i, ans)