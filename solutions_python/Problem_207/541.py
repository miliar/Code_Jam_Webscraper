

for case in xrange(1, int(raw_input()) + 1):
    print 'Case #{}:'.format(case),

    N, R, O, Y, G, B, V = map(int, raw_input().split())
    a = [(R, 'R'), (B, 'B'), (Y, 'Y')]
    a.sort()

    t = [a[2][1]] * a[2][0]

    for i in xrange(a[1][0]):
        t.insert(2*i, a[0][1])

    t.reverse()
    for i in xrange(a[1][0]):
        t.insert(2*i, a[1][1])

    flag = True
    for i in xrange(len(t) - 1):
        if t[i] == t[i+1]:
            flag = False

    print ''.join(t) if flag else 'IMPOSSIBLE'
