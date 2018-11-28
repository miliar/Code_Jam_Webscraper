T = input()

for t in xrange(T):
    line = raw_input()
    ll, K = list(line.split()[0]), int(line.split()[1])

    count = 0
    for i in xrange(len(ll)):
        if ll[i] == '-' and i+K <= len(ll):
            count += 1
            for j in xrange(i, i+K):
                if ll[j] == '-':
                    ll[j] = '+'
                else:
                    ll[j] = '-'


    if all(map(lambda x: x == '+', ll)):
        print 'Case #%d: %d' % (t+1, count)
    else:
        print 'Case #%d: %s' % (t+1, 'IMPOSSIBLE')
