# trying to get quick points :)

t = int(raw_input())

for i in xrange(t):
    x, r, c = map(int, raw_input().split())

    can_fill = False

    if (x == 1):
        can_fill = True
    elif (r < x - 1 or c < x - 1):
        can_fill = False
    elif not (r * c % x == 0):
        can_fill = False
    elif (r % x == 0 or c % x == 0):
        can_fill = True

    if (can_fill):
        res = 'GABRIEL'
    else:
        res = 'RICHARD'

    print 'Case #%s:' % (i + 1), res
