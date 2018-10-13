for t in xrange(input()):
    _, people = raw_input().split()
    people = map(int, iter(people))
    up = 0
    friends = 0
    for shyness, group in enumerate(people):
        needed = max(0, shyness - up)
        friends += needed
        up += needed + group
    print 'Case #%d: %d' % (t + 1, friends)
