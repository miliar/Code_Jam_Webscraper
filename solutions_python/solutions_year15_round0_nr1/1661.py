T = int(raw_input())

for case in xrange(T):

    line = raw_input().split()

    smax = int(line[0])
    peps = map(int, line[1])

    friends = 0
    sum = peps[0]

    for i in xrange(1, smax + 1):
        if sum < i:
            friends += i - sum
            sum += i - sum
        sum += peps[i]


    print 'Case #%d: %d' % (case + 1, friends)
