def magic():
    for t in xrange(input()):
        x = input()
        a = []
        for i in xrange(4):
            z = map(int,raw_input().split())
            a.append(z)
        y = input()
        b = []
        for i in xrange(4):
            z = map(int,raw_input().split())
            b.append(z)
        p = a[x-1][:]
        r = b[y-1][:]
        res = []
        for i in p:
            if i in r:
                res.append(i)
        if len(res) == 1:
            print 'Case #%d: %d'%((t+1),res[0])
        elif len(res) == 0:
            print 'Case #%d: Volunteer cheated!'%(t+1)
        else:
            print 'Case #%d: Bad magician!'%(t+1)
magic()
