
import sys

in_ = sys.stdin
T = int(in_.readline())
for t in xrange(T):
    r1 = int(in_.readline())
    a1 = [map(int, in_.readline().split(' ')) for i in xrange(4)]
    r2 = int(in_.readline())
    a2 = [map(int, in_.readline().split(' ')) for i in xrange(4)]
    res = set(a1[r1 - 1]).intersection(a2[r2 - 1])
    prefix = 'Case #%d:' % (t + 1)
    if len(res) == 1:
        print prefix, list(res)[0]
    elif len(res) > 1:
        print prefix, 'Bad magician!'
    else:
        print prefix, 'Volunteer cheated!'
