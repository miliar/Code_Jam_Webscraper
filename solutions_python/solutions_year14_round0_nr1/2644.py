
T = int(raw_input())

for t in xrange(T):
    
    x = int(raw_input())
    first = [map(int, raw_input().split()) for _ in xrange(4)]

    y = int(raw_input())
    second = [map(int, raw_input().split()) for _ in xrange(4)]

    row1 = set(first[x-1])
    row2 = set(second[y-1])
    cards = row1 & row2

    if len(cards) == 1:
        print 'Case #%d: %d' % (t+1, list(cards)[0])
    elif len(cards) == 0:
        print 'Case #%d: Volunteer cheated!' % (t+1,)
    else:
        print 'Case #%d: Bad magician!' % (t+1,)
