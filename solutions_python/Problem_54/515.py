def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for i in xrange(1, int(raw_input())+1):
    y=0
    n = map(int, raw_input().split())
    N = n[0]
    events = n[1:]
    me = min(events)
    greatest_common = reduce(gcd, map(lambda x: x-me, events))
    if me % greatest_common == 0:
        y=0
    else:
        y= greatest_common - (me % greatest_common)

    print 'Case #%d: %d' % (i, y)
