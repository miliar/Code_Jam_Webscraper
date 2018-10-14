with open('input') as f:
    ts = int(f.readline())
    for t in xrange(1, ts+1):
        line = f.readline()
        [ s_max, n ] = line.split(' ')
        s_max = int(s_max)
        s_counts = [ int(i) for i in n.strip() ]

        i = 0
        standing = 0
        friends = 0
        for s_count in s_counts:
            if standing + friends < i:
                friends = i - standing

            standing += s_count
            i += 1

        print 'Case #%i: %i' % (t, friends)
