rl = lambda: map(int, raw_input().split())

t = input()
for i in xrange(t):
    a = input()
    sa = set([rl() for _ in xrange(4)][a - 1])
    b = input()
    sb = set([rl() for _ in xrange(4)][b - 1])
    sr = sa & sb
    print "Case #%d:" % (i + 1),
    if len(sr) > 1:
        print "Bad magician!"
    elif len(sr) == 0:
        print "Volunteer cheated!"
    else:
        print next(iter(sr))
