for i in xrange(input()):
    r1 = [0, 0, 0, 0]
    r2 = [0, 0, 0, 0]

    a = input()
    for x in xrange(4):
        r1[x] = map(int, raw_input().split())

    b = input()
    for x in xrange(4):
        r2[x] = map(int, raw_input().split())

    intersection = list(set(r1[a - 1]) & set(r2[b - 1]))
    if len(intersection) == 1:
        print "Case #%d: %d" % (i + 1, intersection[0])
    elif len(intersection) == 0:
        print "Case #%d: Volunteer cheated!" % (i + 1)
    else:
        print "Case #%d: Bad magician!" % (i + 1)
