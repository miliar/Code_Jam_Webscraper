import sys

f = sys.stdin

t = int(f.readline())
for i in xrange(t):
    r0 = int(f.readline())
    a0 = []
    for j in xrange(4):
        a0.append(map(int, f.readline().split()))

    xs = set(a0[r0-1])

    r1 = int(f.readline())
    a1 = []
    for j in xrange(4):
        a1.append(map(int, f.readline().split()))

    ys = xs.intersection(a1[r1-1])

    if len(ys) == 1:
        print 'Case #%d: %d' % (i+1, list(ys)[0])
    elif len(ys) > 1:
        print 'Case #%d: Bad magician!' % (i+1, )
    else:
        print 'Case #%d: Volunteer cheated!' % (i+1, )
