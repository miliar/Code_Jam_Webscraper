raw_input = open("A-large.in.txt").readline

for t in xrange(int(raw_input())):
    data = raw_input().split()

    m, c = (int(data[0]), [int(c) for c in data[1]])

    thus = 0
    delta = 0
    for i in xrange(m + 1):
        if c[i] != 0:
            delta += max(0, i - thus)
            thus += c[i] + max(0, i - thus)

    print "Case #%d: %d" % (t + 1, delta)
