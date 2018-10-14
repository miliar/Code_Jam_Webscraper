t = int(raw_input())

x = 1
for _ in xrange(t):
    smax, s = raw_input().split(" ")
    smax = int(smax)

    y = 0
    total = 0
    for i, si in enumerate([int(i) for i in s]):
        if i >= total:
            y += (i - total)
            total += (i - total)
        total += si

    print "Case #{}: {}".format(x, y)
    x += 1
