t = int(raw_input())
for x in xrange(1,t + 1):
    q1 = int(raw_input())
    m1 = [raw_input().split(' ') for y in xrange(0, 4)]
    q2 = int(raw_input())
    m2 = [raw_input().split(' ') for y in xrange(0, 4)]
    count = 0
    card = 0;
    for y in m1[q1 - 1]:
        if y in m2[q2 - 1]:
            card = int(y)
            count = count + 1
    if count == 0:
        print 'Case #%d: %s' % (x,'Volunteer cheated!')
    elif count == 1:
        print 'Case #%d: %d' % (x, card)
    else:
        print 'Case #%d: %s' % (x, 'Bad magician!')