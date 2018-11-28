t = int(raw_input())
for i in xrange(t):
    s1 = int(raw_input()) - 1
    sets1 = [set([int(_) for _ in raw_input().split()]) for j in xrange(4)]
    s2 = int(raw_input()) - 1
    sets2 = [set([int(_) for _ in raw_input().split()]) for j in xrange(4)]
    res = sets1[s1].intersection(sets2[s2])
    if len(res) == 0:
        print 'Case #%i: Volunteer cheated!' % (i + 1)
    elif len(res) == 1:
        print 'Case #%i: ' % (i + 1) + str(res.pop())
    else:
        print 'Case #%i: Bad magician!' % (i + 1)