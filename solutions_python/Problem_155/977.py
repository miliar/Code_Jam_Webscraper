T = int(raw_input().strip())

for i in xrange(T):
    smax, tmp = raw_input().strip().split(' ')
    smax = int(smax)
    sis = map(int, [char for char in tmp])
    need, total = 0, 0
    for j, si in enumerate(sis):
        if total < j:
            jump = j - total
            need += jump
            total += jump
        total += si

    print "Case #%s: %s" % (i + 1, need)
