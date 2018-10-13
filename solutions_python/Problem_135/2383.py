N = input()
for n in xrange(N):
    A = input()
    for i in xrange(1, 5):
        line = raw_input()
        if i == A:
            first = set(line.split())
    B = input()
    for i in xrange(1, 5):
        line = raw_input()
        if i == B:
            second = set(line.split())
    intersect = first & second
    L = len(intersect)
    if L == 0:
        print 'Case #{}: Volunteer cheated!'.format(n + 1)
    elif L > 1:
        print 'Case #{}: Bad magician!'.format(n + 1)
    else:
        print 'Case #{}: {}'.format(n + 1, list(intersect)[0])
