#freaking. amazing.
for c in xrange(input()):
    n = input()
    vs = sorted(map(int, raw_input().split()))
    if reduce(lambda a, b: a^b, vs) == 0:
        print "Case #%d: %d" % (c+1, sum(vs[1:]))
    else:
        print "Case #%d: NO" % (c+1)