t = int(raw_input())

for asdf in xrange(t):
    x = int(raw_input())
    row1 = [map(int, raw_input().split()) for i in range(4)]
    row1 = set(row1[x-1])
    y = int(raw_input())
    row2 = [map(int, raw_input().split()) for i in range(4)]
    row2 = set(row2[y-1])

    card = row2.intersection(row1)
    card = list(card)
    if len(card) == 1:
        print "Case #%d: %d" % (asdf + 1, card[0])
    elif len(card) == 0:
        print "Case #%d: Volunteer cheated!" % (asdf + 1)
    else:
        print "Case #%d: Bad magician!" % (asdf + 1)



