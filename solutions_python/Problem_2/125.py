filename = "B-large.in"
f = open(filename, 'r')
of = open('B-large.out', 'w')

N = int(f.readline())
for i in xrange(N):
    T = int(f.readline())
    AtoB = []
    BtoA = []
    l = f.readline().strip().split(' ')
    NA = int(l[0])
    NB = int(l[1])
    A_events = []
    B_events = []
    for x in xrange(NA):
        l = f.readline().strip().split(' ')
        d, a = l[0].split(':'), l[1].split(':')
        d, a = int(d[0])*60 + int(d[1]), int(a[0])*60 + int(a[1])
        AtoB.append((d, a))
        A_events.append((d, 1))
        B_events.append((a + T, -1))
    for x in xrange(NB):
        l = f.readline().strip().split(' ')
        d, a = l[0].split(':'), l[1].split(':')
        d, a = int(d[0])*60 + int(d[1]), int(a[0])*60 + int(a[1])
        BtoA.append((d, a))
        B_events.append((d, 1))
        A_events.append((a + T, -1))
    A, B = 0, 0
    AtoB.sort()
    BtoA.sort()
    A_events.sort()
    B_events.sort()
    A_surplus, B_surplus = 0, 0
    for x in A_events:
        if(x[1] == -1):
            A_surplus += 1
        else:
            if(A_surplus == 0):
                A += 1
            else:
                A_surplus -= 1
    for x in B_events:
        if(x[1] == -1):
            B_surplus += 1
        else:
            if(B_surplus == 0):
                B += 1
            else:
                B_surplus -= 1

    print AtoB
    print BtoA
    print A_events
    print B_events
    print >> of, 'Case #%d: %d %d' % (i + 1, A, B)
    print '------------------------------------------------------------'
f.close()
of.close()
