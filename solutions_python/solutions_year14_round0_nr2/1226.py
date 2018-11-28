import sys, math

def total(k, c, f, x):
    y = 0.
    for n in xrange(k):
        y += c / (2 + n * f)
    y += x / (2 + k * f)
    return y

fp = sys.stdin

t = int(fp.readline())
for i in xrange(t):
    c, f, x = map(float, fp.readline().split())

    b = (x * f - 2. * c) / f / c
    b = max(0., b)
    b1, b2 = int(b), int(math.ceil(b))
    t1, t2 = total(b1, c, f, x), total(b2, c, f, x)
    if t1 < t2:
        print 'Case #%d: %.7f' % (i+1, t1)
    else:
        print 'Case #%d: %.7f' % (i+1, t2)
